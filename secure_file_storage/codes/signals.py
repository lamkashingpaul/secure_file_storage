from members.models import MyCloudUser
from .models import Code
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=MyCloudUser)
def post_save_generate_code(sender, instance, created, **kwargs):
    if created:
        Code.objects.create(user=instance)
