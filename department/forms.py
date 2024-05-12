from django import forms
from .models import Department

class DepartmentsForm(forms.ModelForm):
  class Meta:
    model = Department
    fields = ['departmentId','departmentName']