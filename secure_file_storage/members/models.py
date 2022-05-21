from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class MyCloudUser(AbstractUser):
    # phone_number = models.CharField(max_length=12)
    phone_number = PhoneNumberField()
