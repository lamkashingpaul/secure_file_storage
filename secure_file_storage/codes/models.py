from django.db import models
from members.models import MyCloudUser
from random import randint
# Create your models here.


class Code(models.Model):
    number = models.CharField(max_length=6, blank=True)
    user = models.OneToOneField(MyCloudUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        self.number = ''.join(str(randint(0, 9)) for _ in range(6))
        super().save(*args, **kwargs)
