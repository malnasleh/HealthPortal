# urls.py
from django.urls import path
from django.contrib import admin
from . import views
from Utils.views import redirect_view

app_name = "healthApp"
urlpatterns = [
    path("patient_dashboard/", views.PatientHomepage.as_view(), name="patientDashboard"),
    path("patient_dashboard/Prescriptions", views.PrescriptionView.as_view(), name="prescriptions"),
    path("patient_dashboard/updatePatientInfo", views.UpdatePatientInfoView.as_view(), name='healthApp-updateInfo'),
    path("patient_dashboard/PatientInfo", views.PatientInfoView.as_view(), name="patientInfo"),
    path("patient_dashboard/DoctorInfo", views.DoctorInfoView.as_view()),
    path("patient_dashboard/InsuranceCoverageInfo", views.InsuranceCoverageInfoView.as_view(), name="coverageInfo"),
    path("patient_dashboard/ProcedureInfo", views.ProcedureInfoView.as_view()),
    path("patient_dashboard/InsuranceAI", views.InsuranceAI.as_view()),
    path("doctor_dashboard/", views.DoctorHomepage.as_view(), name='doctorDashboard'),
    path("doctor_dashboard/MedicationInfo", views.AllMedicationsView.as_view()),
    path("doctor_dashboard/WorksAtInfo", views.WorksAtInfoView.as_view(), name="worksAtInfo"),
    path("doctor_dashboard/ProcedureInfo", views.DoctorProceduresInfoView.as_view(), name="doctorProcedureInfo"),
    path("doctor_dashboard/PrescriptionsDoctorInfo", views.PrescriptionDoctorInfoView.as_view(), name="doctorPrescriptionInfo"),
    path("doctor_dashboard/ManufacturedByInfo", views.DrugManufacturerDoctorInfoView.as_view()),
    path("doctor_dashboard/DoctorViewPatientsView", views.DoctorViewPatientsView.as_view(), name="doctorViewPatients"),
    path("doctor_dashboard/ViewHospitals", views.DoctorViewHospitals.as_view(), name="doctorViewPatients")


]
