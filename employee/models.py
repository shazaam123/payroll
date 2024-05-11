from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  class Meta:
    abstract = True

class Employee(BaseModel):
  employee_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  phone_number = models.CharField(max_length=15)
  address = models.CharField(max_length=255)
  role = models.CharField(max_length=50)
  salary_details = models.ManyToManyField('SalaryDetail', blank=True)
  tax_details = models.ManyToManyField('TaxDetail', blank=True)
  benefits = models.ManyToManyField('Benefit', blank=True)
  attendance = models.ManyToManyField('Attendance', blank=True)
  payroll_history = models.ManyToManyField('PayrollHistory', blank=True)
  user = models.OneToOneField('User', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'