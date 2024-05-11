from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  class Meta:
    abstract = True

class Payroll(BaseModel):
  payroll_history_id = models.AutoField(primary_key=True)
  #employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  pay_date = models.DateField()
  gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
  net_salary = models.DecimalField(max_digits=10, decimal_places=2)
  pay_method = models.CharField(max_length=50)