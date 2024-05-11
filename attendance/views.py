from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Attendance
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_attendance(request):
  if request.method == 'POST':
    employee_id = request.POST.get('employee_id')
    date_log = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')
    am_in = request.POST.get('am_in')
    remarks = request.POST.get('remarks')
    am_in_mask = request.POST.get('am_in_mask')
    am_out = request.POST.get('am_out')
    am_out_mask = request.POST.get('am_out_mask')
    pm_in = request.POST.get('pm_in')
    pm_in_mask = request.POST.get('pm_in_mask')
    pm_out = request.POST.get('pm_out')
    pm_out_mask = request.POST.get('pm_out_mask')

    attendance = Attendance(
      employee_id=employee_id,
      date_log=date_log,
      am_in=am_in,
      am_in_mask=am_in_mask,
      am_out=am_out,
      am_out_mask=am_out_mask,
      pm_in=pm_in,
      pm_in_mask=pm_in_mask,
      pm_out=pm_out,
      pm_out_mask=pm_out_mask,
      remarks=remarks
    )

    attendance.save()

    if attendance.pk:
      result = {
        'status': 'success',
        'message': 'Employee log saved.',
        'attendance_id': attendance.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status': 'error',
        'message': 'Error saving employee log.'
      }
      return JsonResponse(result, status=500)

  elif request.method == 'GET':
    return render(request, 'attendance/save_attendance.html', {})
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])


