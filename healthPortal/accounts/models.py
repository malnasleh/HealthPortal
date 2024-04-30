from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, healthID, password, email=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(healthID=healthID, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, healthID, password, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(healthID = healthID, password=password, email = email, **extra_fields)

    def create_superuser(self, healthID, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(healthID=healthID, password=password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    healthID = models.CharField(max_length=9, validators=[RegexValidator(
        regex='^[0-9]+$',
        message='Only digits (0-9) are allowed.',
        code='invalid_your_field'
    ), MinLengthValidator(9)], unique=True)
    USER_ROLES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    userKind = models.CharField(
        max_length=10, choices=USER_ROLES, default='patient')
    Age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)], default=25)
    Phone_num = models.CharField(max_length=10, validators=[
                                 MinLengthValidator(10)], default="9991113333")
    Address = models.CharField(max_length=500, default="No Address On Record")
    USERNAME_FIELD = 'healthID'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return str(self.username)
