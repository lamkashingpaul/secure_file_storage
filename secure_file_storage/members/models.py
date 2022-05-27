from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class MyCloudUser(AbstractUser):
    phone_number = PhoneNumberField()
