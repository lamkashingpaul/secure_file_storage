from django.contrib.auth.forms import UserCreationForm
from .models import MyCloudUser
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyCloudUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
