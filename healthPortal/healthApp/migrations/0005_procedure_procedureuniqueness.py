# Generated by Django 4.2.7 on 2023-11-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthApp', '0004_alter_procedure_procedure_id'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='procedure',
            constraint=models.UniqueConstraint(fields=('Procedure_Date', 'Patient_Health_ID'), name='ProcedureUniqueness'),
        ),
    ]
