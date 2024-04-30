# Generated by Django 4.2.7 on 2023-11-27 20:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Medical_ID_Number', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Name', models.CharField(max_length=255)),
                ('Phone_num', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('Email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Drug_Manufacturer',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=500)),
                ('Phone_num', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('Hospital_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=355)),
                ('Address', models.CharField(max_length=500)),
                ('Phone_num', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Insurance_Company',
            fields=[
                ('Insurance_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=500)),
                ('Phone_num', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('DIN', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Cost', models.FloatField()),
                ('Dosage', models.CharField(max_length=750)),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('health_ID', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Email', models.CharField(max_length=255)),
                ('Age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('FName', models.CharField(max_length=255)),
                ('MName', models.CharField(max_length=255)),
                ('LName', models.CharField(max_length=255)),
                ('Phone_num', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('Address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Specialties',
            fields=[
                ('Doctor_Medical_ID_Number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='healthApp.doctor')),
                ('Specialty', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Works_At',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.hospital')),
                ('Medical_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('Procedure_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Procedure_Date', models.DateTimeField()),
                ('Procedure_Type', models.CharField(max_length=255)),
                ('Duration_hours', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Result', models.CharField(max_length=255)),
                ('Hospital_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.hospital')),
                ('Patient_Health_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescribes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Medical_ID_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.doctor')),
                ('Medication_DIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.medication')),
                ('Patient_Health_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Oversees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Medical_ID_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.doctor')),
                ('Procedure_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Manufactured_By',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.medication')),
                ('Drug_Manufacturer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.drug_manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance_Policy',
            fields=[
                ('Policy_id', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Coverage', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Monthly_Cost', models.IntegerField()),
                ('Insurance_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.insurance_company')),
            ],
        ),
        migrations.CreateModel(
            name='Covers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.medication')),
                ('Insurance_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.insurance_company')),
                ('Policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.insurance_policy')),
            ],
        ),
        migrations.CreateModel(
            name='Covered_By',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Health_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.patient')),
                ('Insurance_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.insurance_company')),
                ('Policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.insurance_policy')),
            ],
        ),
        migrations.CreateModel(
            name='CaresFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Medical_ID_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.doctor')),
                ('Patient_Health_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthApp.patient')),
            ],
        ),
        migrations.AddConstraint(
            model_name='works_at',
            constraint=models.UniqueConstraint(fields=('Medical_ID', 'Hospital_ID'), name='WorksAt_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='prescribes',
            constraint=models.UniqueConstraint(fields=('Doctor_Medical_ID_Number', 'Patient_Health_ID', 'Medication_DIN'), name='Prescribes_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='oversees',
            constraint=models.UniqueConstraint(fields=('Procedure_ID', 'Doctor_Medical_ID_Number'), name='Oversees_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='manufactured_by',
            constraint=models.UniqueConstraint(fields=('DIN', 'Drug_Manufacturer_Id'), name='ManufacturedBy_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='covers',
            constraint=models.UniqueConstraint(fields=('Insurance_name', 'Policy_id', 'DIN'), name='Covers_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='covered_by',
            constraint=models.UniqueConstraint(fields=('Health_ID', 'Insurance_name', 'Policy_id'), name='CoveredBy_pk_constraint'),
        ),
        migrations.AddConstraint(
            model_name='caresfor',
            constraint=models.UniqueConstraint(fields=('Patient_Health_ID', 'Doctor_Medical_ID_Number'), name='CaresFor_pk_constraint'),
        ),
    ]
