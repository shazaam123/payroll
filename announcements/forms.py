from django import forms
from .models import GeneralAnnouncement, EventAnnouncement, JobAnnouncement, EmergencyAnnouncement, MaintenanceAnnouncement

class GeneralAnnouncementForm(forms.ModelForm):
  class Meta:
    model = GeneralAnnouncement
    fields = ['title', 'content', 'image', 'publish_date', 'expiry_date', 'priority']

class EventAnnouncementForm(forms.ModelForm):
  class Meta:
    model = EventAnnouncement
    fields = ['title', 'content', 'expiry_date', 'location', 'event_date', 'registration_deadline', 'registration_link']

class JobAnnouncementForm(forms.ModelForm):
  class Meta:
      model = JobAnnouncement
      fields = ['title', 'content', 'expiry_date', 'location', 'job_type', 'salary', 'application_deadline', 'application_link']

class EmergencyAnnouncementForm(forms.ModelForm):
  class Meta:
      model = EmergencyAnnouncement
      fields = ['title', 'content', 'expiry_date', 'urgency_level', 'affected_area', 'instructions']

class MaintenanceAnnouncementForm(forms.ModelForm):
  class Meta:
      model = MaintenanceAnnouncement
      fields = ['title', 'content', 'expiry_date', 'affected_system', 'maintenance_period', 'contact_information']