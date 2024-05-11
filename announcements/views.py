from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse
from payroll.forms import AnnouncementForm
from .forms import GeneralAnnouncementForm, EventAnnouncementForm, JobAnnouncementForm, EmergencyAnnouncementForm, MaintenanceAnnouncementForm
from .models import GeneralAnnouncement, EventAnnouncement, JobAnnouncement, EmergencyAnnouncement, MaintenanceAnnouncement


class PostAnnouncementView(CreateView):
    template_name = 'templates/post_announcement.html'
    success_url = ('/success_page')


def post_announcement(request):
    if request.method == 'POST':
        announce_type = request.POST['announcement_type']
        if announce_type == 'general':
            form = AnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                announcement = GeneralAnnouncement(**form.cleaned_data)
                announcement.save()
                return redirect(reverse('success_page'))

        elif announce_type == 'event':
            form = EventAnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                announcement = EventAnnouncement(**form.cleaned_data)
                announcement.save()
                return redirect(reverse('success_page'))

        elif announce_type == 'job':
            form = JobAnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                announcement = JobAnnouncement(**form.cleaned_data)
                announcement.save()
                return redirect(reverse('success_page'))

        elif announce_type == 'emergency':
            form = EmergencyAnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                announcement = EmergencyAnnouncement(**form.cleaned_data)
                announcement.save()
                return redirect(reverse('success_page'))

        else:
            form = MaintenanceAnnouncementForm(request.POST, request.FILES)
            if form.is_valid():
                announcement = MaintenanceAnnouncement(**form.cleaned_data)
                announcement.save()
                return redirect(reverse('success_page'))

    else:
        return render(request, 'templates/post_announcement.html')


def success_page(request):
    if request.method == 'GET':
        return render(request, 'templates/success_page.html')
