from django.db import models
from django.utils import timezone
from employee.models import Employee

class BaseModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  class Meta:
      abstract = True

class Benefit(BaseModel):
  benefit_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  benefit_type = models.CharField(max_length=100)
  benefit_amount = models.DecimalField(max_digits=10, decimal_places=2)
  benefit_description = models.TextField()