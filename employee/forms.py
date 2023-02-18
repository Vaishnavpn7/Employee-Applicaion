from django import forms
from employee.models import Employees
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()