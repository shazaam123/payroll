from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    priority = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
      return str(self.title)

class GeneralAnnouncement(BaseModel):
    image = models.ImageField(upload_to='announcements/general/', blank=True, null=True)

class EventAnnouncement(BaseModel):
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    registration_deadline = models.DateTimeField()
    registration_link = models.URLField(blank=True)

class JobAnnouncement(BaseModel):
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    application_deadline = models.DateTimeField()
    application_link = models.URLField()

class EmergencyAnnouncement(BaseModel):
    urgency_level = models.CharField(max_length=100)
    affected_area = models.TextField()
    instructions = models.TextField()

class MaintenanceAnnouncement(BaseModel):
    affected_system = models.TextField()
    maintenance_period = models.DateTimeField()
    contact_information = models.TextField()
