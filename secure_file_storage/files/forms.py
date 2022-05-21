from django import forms
from django.forms import ModelForm
from .models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']
        labels = {
            'name': 'Name',
            'file': 'File',
        }
        help_texts = {
            'name': 'Name of the file',
            'file': 'Select the file',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
