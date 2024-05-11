from django import forms
from .models import Employee

class EmployeeCreationForm(forms.ModelForm):
   class Meta:
     model = Employee
     fields = ['first_name', 'last_name', 'gender', 'address', 'email', 'phone', 'department', 'position']
     widget = {
       'date_of_birth': forms.DateInput(attrs={'type':'date'}),
       'hire_date': forms.DateInput(attrs={'type':'date'})
     }

class EmployeeUpdateForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = ['first_name', 'last_name', 'gender', 'address', 'email', 'phone', 'department', 'position']

    widget = {
      'date_of_birth': forms.DateInput(attrs={'type':'date'}),
      'hire_date': forms.DateInput(attrs={'type':'date'})
    }