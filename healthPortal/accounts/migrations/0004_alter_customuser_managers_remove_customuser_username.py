# Generated by Django 4.2.7 on 2023-11-28 06:42

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_healthid'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]