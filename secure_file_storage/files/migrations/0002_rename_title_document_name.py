# Generated by Django 4.0.4 on 2022-05-19 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='name',
        ),
    ]
