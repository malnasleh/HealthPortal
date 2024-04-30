
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Patient, Doctor


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created and (instance.userKind == 'patient'):
        Patient.objects.create(health_ID=instance.healthID, Age=instance.Age, Phone_num=instance.Phone_num, Address=instance.Address, FName=instance.first_name, LName=instance.last_name, Email=instance.email)
    elif created and  (instance.userKind == 'doctor'):
        Doctor.objects.create(Medical_ID_Number=instance.healthID, Name=(instance.first_name + ' ' + instance.last_name), Phone_num=instance.Phone_num, Email=instance.email)
