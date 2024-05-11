from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)

  class Meta:
    abstract = True

class Department(BaseModel):
  departmentId = models.AutoField(primary_key=True)
  departmentName = models.CharField(max_length=255)


class Employee(BaseModel):
  employee_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  gender = models.CharField(max_length=1)
  address = models.CharField(max_length=255)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  position = models.CharField(max_length=100)
  hire_date = models.DateField()


class SalaryDetail(BaseModel):
  salary_detail_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
  allowances = models.DecimalField(max_digits=10, decimal_places=2)
  deductions = models.DecimalField(max_digits=10, decimal_places=2)
  net_salary = models.DecimalField(max_digits=10, decimal_places=2)
  pay_period_start = models.DateField()
  pay_period_end = models.DateField()


class TaxDetail(BaseModel):
  tax_detail_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  tax_type = models.CharField(max_length=100)
  tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
  taxable_income = models.DecimalField(max_digits=10, decimal_places=2)


class Benefit(BaseModel):
  benefit_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  benefit_type = models.CharField(max_length=100)
  benefit_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Attendance(BaseModel):
  attendance_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  attendance_date = models.DateField()
  check_in_time = models.DateTimeField()
  check_out_time = models.DateTimeField()


class PayrollHistory(BaseModel):
  payroll_history_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  pay_date = models.DateField()
  gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
  net_salary = models.DecimalField(max_digits=10, decimal_places=2)
  pay_method = models.CharField(max_length=50)

class User(BaseModel):
  user_id = models.AutoField(primary_key=True)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  username = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=100)
  last_login = models.DateTimeField()
  ROLE_CHOICES = [
      ('Employee', 'Employee'),
      ('Admin', 'Admin'),
  ]
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Announcement(BaseModel):
  announcement_id = models.AutoField(primary_key=True)
  announcement_date = models.DateField()
  title = models.CharField(max_length=255)
  content = models.TextField()
