from django import forms
from django.db.models import fields
from .models import Benefit
from employee.models import Employee

class BenefitForm(forms.ModelForm):
  class Meta:
    model = Benefit
    fields = ['benefit_id', 'employee_id', 'benefit_type', 'benefit_amount', 'benefit_description']