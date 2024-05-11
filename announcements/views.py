from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from payroll.forms import AnnouncementForm
from .forms import GeneralAnnouncementForm, EventAnnouncementForm, JobAnnouncementForm, EmergencyAnnouncementForm, MaintenanceAnnouncementForm
from .models import GeneralAnnouncement, EventAnnouncement, JobAnnouncement, EmergencyAnnouncement, MaintenanceAnnouncement

def post_announcement(request):
  if request.method == 'POST':
    announce_type = request.POST[announcement_type]
    if announce_type == 'general':
      form = AnnouncementForm(request.POST, request.FILES)
      if form.is_valid():
        announcement = GeneralAnnouncement(**form.cleaned_data)
        announcement.save()
        return redirect(announcement)

    elif announce_type == 'event':
      form = EventAnnouncementForm(request.POST, request.FILES)
      if form.is_valid():
        announcement = EventAnnouncement(**form.cleaned_data)
        announcement.save()
        return redirect(announcement)

    elif announce_type == 'job':
      form = JobAnnouncementForm(request.POST, request.FILES)
      