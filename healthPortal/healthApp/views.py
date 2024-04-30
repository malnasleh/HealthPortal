from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import PatientInfoForm, CoverageForm, HospitalForm, ProcedureForm, PrescriptionForm
from .models import *
from scipy.stats import linregress

# Patient Views


class patientAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userKind == 'patient'

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')
        message = "You do not have permission to access this page as you are not a patient. Please <a href='/redirect/doctor_dashboard'>go to the doctor homepage</a>"
        return HttpResponseForbidden(message)


class PatientHomepage(patientAccessMixin, TemplateView):
    def get(self, request):
        try:
            patient = Patient.objects.get(health_ID=request.user.healthID)
        except ObjectDoesNotExist:
            return redirect('login')
        context = {'currentPatient': patient, }
        return render(request, 'healthApp/Patient.html', context)


class PatientInfoView(patientAccessMixin, TemplateView):
    def get(self, request):
        querySet = Patient.objects.filter(health_ID=request.user.healthID)
        context = {'patientInfo': querySet, }
        return render(request, "healthApp/PatientInfo.html", context)


class UpdatePatientInfoView(patientAccessMixin, TemplateView):
    def get(self, request):
        form = PatientInfoForm(instance=Patient.objects.get(
            health_ID=request.user.healthID))

        return render(request, 'healthApp/updatePatientInfo.html', {'form': form})

    def post(self, request):
        form = PatientInfoForm(request.POST, instance=Patient.objects.get(health_ID=request.user.healthID))
        if form.is_valid():
            form.save()
            return redirect('healthApp:patientInfo')
        else:
            messages.error(request, 'ERROR! The form is not valid.')
            return render(request, 'healthApp/updatePatientInfo.html', {'form': form})


class DoctorInfoView(patientAccessMixin, TemplateView):
    def get(self, request):
        querySet = CaresFor.objects.filter(
            Patient_Health_ID=request.user.healthID)
        context = {'care_relationship_list': querySet, }
        return render(request, "healthApp/DoctorInfo.html", context)


class ProcedureInfoView(patientAccessMixin, TemplateView):
    def get(self, request):
        querySet = Procedure.objects.filter(
            Patient_Health_ID=request.user.healthID)
        context = {'procedure_list': querySet, }
        return render(request, "healthApp/ProcedureInfo.html", context)


class InsuranceCoverageInfoView(patientAccessMixin, TemplateView):
    def get(self, request):
        form = CoverageForm()
        querySet = Covered_By.objects.filter(Health_ID=request.user.healthID)
        context = {'coverage_list': querySet, "form": form}
        return render(request, "healthApp/InsuranceCoverage.html", context)

    def post(self, request):
        form = CoverageForm(request.POST)
        if form.is_valid():
            selected_policy = form.cleaned_data['insurance_policy']
            health_id = Patient.objects.get(health_ID=request.user.healthID)
            insurance_name = selected_policy.Insurance_name
            policy_id = selected_policy
            if 'add_button' in request.POST:
                try:
                    Covered_By.objects.create(
                        Health_ID=health_id,
                        Insurance_name=insurance_name,
                        Policy_id=policy_id
                    )
                except IntegrityError:
                    messages.error(
                        request, 'ERROR! You are already covered by this insurance policy.')
            elif 'delete_button' in request.POST:
                Covered_By.objects.filter(
                    Policy_id=policy_id, Health_ID=health_id).delete()
            return redirect('healthApp:coverageInfo')

class InsuranceAI(patientAccessMixin, TemplateView):
    def get(self, request):
        cs = Covered_By.objects.filter(Health_ID=request.user.healthID)
        costVsCoverage = [(c.Policy_id.Coverage, c.Policy_id.Monthly_Cost) for c in cs]
        if len(costVsCoverage) <= 1:
            messages.error(request, "Unfortunately, you don't have enough insurance policies so we cannot estimate expected costs.")
            return render(request, "healthApp/InsuranceAI.html", {'coverage_list':[]})
        else:
            reg = linregress(*zip(*costVsCoverage))
            res = []
            for desiredCoverage in range(10, 101, 5):
                expectedCost = (reg.intercept + reg.slope*desiredCoverage)
                if expectedCost > 0:
                    res.append((desiredCoverage, round(expectedCost,2)))
            additionalInfo = ""
            # assuming the line has positive slope, points above it have high cost and below have lower cost than expected
            if reg.slope > 0:
                allPolicies = Insurance_Policy.objects.all()
                cheap = lambda p: p.Monthly_Cost <= p.Coverage*reg.slope + reg.intercept
                cheapOptions = '\n'.join([f"{p.Insurance_name.Insurance_name}: {p.Policy_id} ({p.Coverage}% for ${p.Monthly_Cost}/month)" for p in allPolicies if cheap(p)])
                expensiveOptions = '\n'.join([f"{p.Insurance_name.Insurance_name}: {p.Policy_id} ({p.Coverage}% for ${p.Monthly_Cost}/month)" for p in allPolicies if not cheap(p)])
                additionalInfo = f"""Based on your current insurance policies, the following options are well-priced: 
                {cheapOptions}

                More expensive options include: 
                {expensiveOptions}"""

            context = {'coverage_list':res, 'info':additionalInfo}
            return render(request, "healthApp/InsuranceAI.html", context)


class PrescriptionView(patientAccessMixin, TemplateView):
    def get(self, request):
        form = CoverageForm()
        querySet = Prescribes.objects.filter(
            Patient_Health_ID=request.user.healthID)
        context = {'prescribes_list': querySet,
                   "form": form, "adjusted_costs": None}
        return render(request, "healthApp/Prescriptions.html", context)

    def post(self, request):
        form = CoverageForm(request.POST)
        if form.is_valid():
            querySet = Prescribes.objects.filter(Patient_Health_ID=request.user.healthID)
            selected_policy = form.cleaned_data['insurance_policy']
            adjustedPrices = []
            for prescription in querySet:
                if(len(Covers.objects.filter(DIN = prescription.Medication_DIN, Policy_id = selected_policy)) > 0):
                    adjustedPrices.append(prescription.Medication_DIN.Cost * (1 - (selected_policy.Coverage/100)))
                else:
                    adjustedPrices.append(prescription.Medication_DIN.Cost)
            zippedList = zip(querySet, adjustedPrices)
            context = {'prescribes_list': querySet, "form": form,
                       "zippedMedicationPrice": zippedList}
            return render(request, "healthApp/Prescriptions.html", context)
# End Patient views


# Doctor Views
class doctorAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userKind == 'doctor'

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')
        message = "You do not have permission to access this page as you are not a doctor. Please <a href='/redirect/patient_dashboard'>go to the patient homepage</a>"
        return HttpResponseForbidden(message)


class DoctorHomepage(doctorAccessMixin, View):
    def get(self, request):
        try:
            doctor = Doctor.objects.get(
                Medical_ID_Number=request.user.healthID)
        except ObjectDoesNotExist:
            return redirect('login')
        context = {'currentDoctor': doctor, }
        return render(request, 'healthApp/Doctor.html', context)


class WorksAtInfoView(doctorAccessMixin, TemplateView):
    def get(self, request):
        form = HospitalForm()
        querySet = Works_At.objects.filter(Medical_ID=request.user.healthID)
        context = {'works_at_list': querySet, "form": form}
        return render(request, "healthApp/WorksAtInfo.html", context)

    def post(self, request):
        form = HospitalForm(request.POST)
        if form.is_valid():
            selected_hospital = form.cleaned_data['hospital']
            medical_id = Doctor.objects.get(
                Medical_ID_Number=request.user.healthID)
            hospital_id = selected_hospital
            if 'add_button' in request.POST:
                try:
                    Works_At.objects.create(
                        Medical_ID=medical_id,
                        Hospital_ID=hospital_id
                    )
                except IntegrityError:
                    messages.error(
                        request, 'ERROR! You are already working at this hospital.')
            elif 'delete_button' in request.POST:
                Works_At.objects.filter(
                    Medical_ID=medical_id, Hospital_ID=hospital_id).delete()
            return redirect('healthApp:worksAtInfo')


class DrugManufacturerDoctorInfoView(doctorAccessMixin, TemplateView):
    def get(self, request):
        querySet = Drug_Manufacturer.objects.all()
        context = {'drug_manufacturer_list': querySet, }
        return render(request, "healthApp/DrugManufacturerDoctorInfo.html", context)


class PrescriptionDoctorInfoView(doctorAccessMixin, TemplateView):
    def get(self, request):
        form = PrescriptionForm()
        if 'healthID' in request.GET:
            health_id = request.GET['healthID']
            # Update queryset based on the entered health ID
            querySet = Prescribes.objects.filter(Patient_Health_ID=health_id)
            if len(querySet) == 0:
                messages.error(request, 'No prescriptions exist for patient with healthID: ' +
                               health_id + '. Displaying all of your written prescriptions')
                querySet = Prescribes.objects.filter(
                    Doctor_Medical_ID_Number=request.user.healthID)
        else:
            querySet = Prescribes.objects.filter(
                Doctor_Medical_ID_Number=request.user.healthID)
        context = {'doctor_prescribes_list': querySet, 'form':form}
        return render(request, "healthApp/PrescriptionsDoctorInfo.html", context)
    
    def post(self, request):
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            Patient_selected = form.cleaned_data['Patient_Health_ID']
            Medication_Selected = form.cleaned_data['Medication_DIN']
            currentDoctor = Doctor.objects.get(Medical_ID_Number = request.user.healthID )
            try:
                 Prescribes.objects.create(Doctor_Medical_ID_Number = currentDoctor, Patient_Health_ID = Patient_selected, Medication_DIN = Medication_Selected)
            except IntegrityError:
                messages.error(
                    request, "ERROR! You have already prescribed this medication to this patient.")
            return redirect(reverse("healthApp:doctorPrescriptionInfo"))


class DoctorViewPatientsView(doctorAccessMixin, TemplateView):
    def get(self, request):
        if 'healthID' in request.GET:
            health_id = request.GET['healthID']
            querySet = Patient.objects.filter(health_ID=health_id)
            if len(querySet) == 0:
                messages.error(
                    request, "Couldn't find any patients with requested Health ID. Please double check the entered Health ID.")
        else:
            patientIDs = [cf.Patient_Health_ID.health_ID for cf in CaresFor.objects.filter(
                Doctor_Medical_ID_Number=request.user.healthID)]
            if len(patientIDs) == 0:
                messages.error(
                    request, "Couldn't find any patient that you care for.")
            querySet = Patient.objects.filter(health_ID__in=patientIDs)
            if len(querySet) == 0:
                messages.error(
                    request, "Couldn't find any patients that you care for.")
        context = {"patient_list": querySet}
        return render(request, "healthApp/DoctorViewPatients.html", context)


class DoctorViewHospitals(doctorAccessMixin, TemplateView):
    def get(self, request):
        querySet = Hospital.objects.all()
        return render(request, "healthApp/ViewHospitals.html", {"hospital_list": querySet})


class DoctorProceduresInfoView(doctorAccessMixin, TemplateView):
    def get(self, request):
        form = ProcedureForm()
        related_procedures_list = []
        if 'healthID' in request.GET:
            health_id = request.GET['healthID']
            # Update queryset based on the entered health ID
            querySet = Procedure.objects.filter(Patient_Health_ID=health_id)
            if len(querySet) == 0:
                messages.error(request, 'No prescriptions exist for patient with healthID: ' +
                               health_id + '. Displaying all of your written prescriptions')
                for oversees in Oversees.objects.filter(Doctor_Medical_ID_Number=request.user.healthID):
                    related_procedures_list.append(oversees.Procedure_ID)
                querySet = related_procedures_list
        else:
            for oversees in Oversees.objects.filter(Doctor_Medical_ID_Number=request.user.healthID):
                related_procedures_list.append(oversees.Procedure_ID)
            querySet = related_procedures_list
        context = {'procedure_list': querySet, 'form': form}
        return render(request, "healthApp/ProcedureInfoDoctor.html", context)

    def post(self, request):
        form = ProcedureForm(request.POST)
        if form.is_valid():
            Procedure_Date_entered = form.cleaned_data['Procedure_Date']
            Procedure_Type_entered = form.cleaned_data['Procedure_Type']
            Duration_hours_entered = form.cleaned_data['Duration_hours']
            Name_entered = form.cleaned_data['Name']
            Result_entered = form.cleaned_data['Result']
            Patient_Health_ID_entered = form.cleaned_data['Patient_Health_ID']
            Hospital_ID_entered = form.cleaned_data['Hospital_ID']
            try:
                procedure = Procedure.objects.create(Procedure_Date=Procedure_Date_entered,
                                         Procedure_Type=Procedure_Type_entered, Duration_hours=Duration_hours_entered,
                                         Name=Name_entered, Result=Result_entered, Patient_Health_ID=Patient_Health_ID_entered, Hospital_ID=Hospital_ID_entered)
                Oversees.objects.create(Procedure_ID = procedure, Doctor_Medical_ID_Number = Doctor.objects.get(Medical_ID_Number = request.user.healthID))
            except IntegrityError:
                messages.error(
                    request, "There was an error with the information you entered. Please make sure the procedure details you're entering don't already exist.")
            return redirect(reverse("healthApp:doctorProcedureInfo"))


class AllMedicationsView(doctorAccessMixin, TemplateView):
    def get(self, request):
        querySet = Medication.objects.all()
        context = {'medication_list': querySet, }
        return render(request, "healthApp/MedicationInfo.html", context)
# END Doctor views
