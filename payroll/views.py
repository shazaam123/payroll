from django.shortcuts import render
from .models import Attendance
from datetime import datetime
from django.http import JsonResponse

def save_attendance(request):
  if request.method == 'POST':
    employee_id = request.POST.get('employee_id')
    date_log = request.POST.get('date_log')
    am_in = request.POST.get('am_in')
    am_in_mask = request.POST.get('am_in_mask')
    am_out = request.POST.get('am_out')
    am_out_mask = request.POST.get('am_out_mask')
    pm_in = request.POST.get('pm_in')
    pm_in_mask = request.POST.get('pm_in_mask')
    pm_out = request.POST.get('pm_out')
    pm_out_mask = request.POST.get('pm_out_mask')

    # Accessing the default manager "objects" through the Attendance model's class instance
    attendance = Attendance.objects.all()