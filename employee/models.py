from django.db import models
from django.utils import timezone
from department.models import Department

class BaseModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  class Meta:
    abstract = True

class Employee(BaseModel):
  employee_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('Non-Binary', 'Non-Binary')])
  address = models.CharField(max_length=255)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  position = models.CharField(max_length=100)
  hire_date = models.DateField()

  objects = models.Manager()