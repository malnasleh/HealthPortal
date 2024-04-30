from django import forms
from django.core.validators import MinLengthValidator
from .models import Patient, Insurance_Policy, Hospital, Procedure, Prescribes

class PatientInfoForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['FName', 'MName', 'LName', 'Phone_num', 'Email', 'Age', 'Address']

class CoverageForm(forms.ModelForm):
    class Meta:
        model = Insurance_Policy
        fields = []
    insurance_policy = forms.ModelChoiceField(queryset=Insurance_Policy.objects.all())

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = []
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ['Procedure_Date', 'Procedure_Type', 'Duration_hours', 'Name', 'Result', 'Patient_Health_ID', 'Hospital_ID',]
        labels = {
            'Patient_Health_ID': 'Patient',
            'Hospital_ID': 'Hospital',
        }
        widgets = {'Procedure_Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),}

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescribes
        fields = ['Patient_Health_ID', 'Medication_DIN']
        labels = {
            'Patient_Health_ID': 'Patient',
            'Medication_DIN': 'Medication',
        }
        
