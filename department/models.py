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