from django import forms
from django.contrib.auth.models import User
from django.core import validators

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(), validators=[validators.MinLengthValidator(8)])

  class Meta:
    model = User
    fields = ['username', 'email', 'password']

class EmployeeCreationForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']

class EmployeeResetForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']
  def send_reset_email(self):
    pass