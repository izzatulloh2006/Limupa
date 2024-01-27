from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput
from django import forms
from .models import Emails


class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=255, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password doesn't match")
        return make_password(password)


class EmailForm(forms.ModelForm):
    def clean_email(self):
        email = self.data.get('email')
        if Emails.objects.filter(email=email):
            raise ValidationError('Email already exists !')
        return email

    class Meta:
        model = Emails
        fields = ('email',)




