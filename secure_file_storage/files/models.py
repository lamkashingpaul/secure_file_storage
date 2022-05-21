from django.db import models
from members.models import MyCloudUser
from private_storage.fields import PrivateFileField
import uuid


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = PrivateFileField('File', max_file_size=1048576, upload_subfolder=lambda instance: [instance.user.id, str(uuid.uuid4())])
    user = models.ForeignKey(MyCloudUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
