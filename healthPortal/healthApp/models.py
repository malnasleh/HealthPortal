from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.


class Patient(models.Model):
    health_ID = models.CharField(max_length=9, validators=[MinLengthValidator(9)], primary_key=True)
    Email = models.CharField(max_length=255)
    Age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    FName = models.CharField(max_length=255)
    MName = models.CharField(max_length=255)
    LName = models.CharField(max_length=255)
    Phone_num = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    Address = models.CharField(max_length=500)
    def __str__(self):
        return str(self.FName + ' ' + self.LName + ' (' + self.health_ID + ')')


class Doctor(models.Model):
    Medical_ID_Number = models.CharField(max_length=9, validators=[MinLengthValidator(9)], primary_key=True)
    Name = models.CharField(max_length=255)
    Phone_num = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    Email = models.CharField(max_length=255)
    def __str__(self):
        return str(self.Name + ' (' + self.Medical_ID_Number + ')')


class CaresFor(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Patient_Health_ID', 'Doctor_Medical_ID_Number'], name = 'CaresFor_pk_constraint')]
    Patient_Health_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_Medical_ID_Number = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Procedure(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Procedure_Date', 'Patient_Health_ID'], name = 'ProcedureUniqueness')]
    Procedure_ID = models.AutoField(primary_key=True)
    Procedure_Date = models.DateTimeField()
    Procedure_Type = models.CharField(max_length=255)
    Duration_hours = models.IntegerField()
    Name = models.CharField(max_length=255)
    Result = models.CharField(max_length=255)
    Patient_Health_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Hospital_ID = models.ForeignKey("Hospital", on_delete=models.CASCADE)


class Doctor_Specialties(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Doctor_Medical_ID_Number', 'Specialty'], name = 'Specialties_pk_constraint')]
    Doctor_Medical_ID_Number = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Specialty = models.CharField(max_length=255)
    def __str__(self):
        return str(self.Specialty)


class Hospital(models.Model):
    Hospital_ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=355)
    Address = models.CharField(max_length=500)
    Phone_num = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    def __str__(self):
        return str(self.Name)


class Works_At(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Medical_ID', 'Hospital_ID'], name = 'WorksAt_pk_constraint')]
    Medical_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.CASCADE)


class Oversees(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Procedure_ID', 'Doctor_Medical_ID_Number'], name = 'Oversees_pk_constraint')]
    Procedure_ID = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    Doctor_Medical_ID_Number = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Doctor_Medical_ID_Number.Name)


class Prescribes(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Doctor_Medical_ID_Number', 'Patient_Health_ID', 'Medication_DIN'], name = 'Prescribes_pk_constraint')]
    Doctor_Medical_ID_Number = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient_Health_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medication_DIN = models.ForeignKey("Medication", on_delete=models.CASCADE)


class Covered_By(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Health_ID', 'Insurance_name', 'Policy_id'], name = 'CoveredBy_pk_constraint')]
    Health_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Insurance_name = models.ForeignKey("Insurance_Company", on_delete=models.CASCADE)
    Policy_id = models.ForeignKey("Insurance_Policy", on_delete=models.CASCADE)


class Insurance_Policy(models.Model):
    Policy_id = models.CharField(primary_key=True, max_length=9, validators=[MinLengthValidator(9)])
    Insurance_name = models.ForeignKey("Insurance_Company", on_delete=models.CASCADE)
    Coverage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    Monthly_Cost = models.IntegerField()
    def __str__(self):
        return str(self.Policy_id + ' (Provider: ' + self.Insurance_name.Insurance_name + ')')



class Insurance_Company(models.Model):
    Insurance_name = models.CharField(primary_key=True, max_length=255)
    Address = models.CharField(max_length=500)
    Phone_num = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

class Covers(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['Insurance_name', 'Policy_id', 'DIN'], name = 'Covers_pk_constraint')]
    Insurance_name = models.ForeignKey(Insurance_Company, on_delete=models.CASCADE)
    Policy_id = models.ForeignKey(Insurance_Policy, on_delete=models.CASCADE)
    DIN = models.ForeignKey("Medication", on_delete=models.CASCADE)

class Medication(models.Model):
    DIN = models.CharField(primary_key=True, max_length=9, validators=[MinLengthValidator(9)])
    Cost = models.FloatField()
    Dosage = models.CharField(max_length=750)
    Name = models.CharField(max_length=500)
    def __str__(self):
        return str(self.Name + ' (' + self.DIN + ')')

class Manufactured_By(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields = ['DIN', 'Drug_Manufacturer_Id'], name = 'ManufacturedBy_pk_constraint')]
    DIN = models.ForeignKey(Medication, on_delete=models.CASCADE)
    Drug_Manufacturer_Id = models.ForeignKey("Drug_Manufacturer", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.DIN.Name)

class Drug_Manufacturer(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=500)
    Phone_num = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
