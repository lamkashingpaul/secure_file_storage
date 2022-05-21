from django import forms
from .models import Code


class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter your code', max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Code
        fields = ('number',)
