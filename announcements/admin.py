from django.contrib import admin
from .models import GeneralAnnouncement, EventAnnouncement, JobAnnouncement, EmergencyAnnouncement, MaintenanceAnnouncement

admin.site.register(GeneralAnnouncement)
admin.site.register(EventAnnouncement)
admin.site.register(JobAnnouncement)
admin.site.register(EmergencyAnnouncement)
admin.site.register(MaintenanceAnnouncement)