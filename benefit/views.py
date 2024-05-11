from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Benefit
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_benefit(request):
  if request.method == 'POST':
    benefit_id = request.POST.get('benefit_id')
    employee_id = request.POST.get('employee_id')
    benefit_type = request.POST.get('benefit_type')
    benefit_amount = request.POST.get('benefit_amount')
    benefit_description = request.POST.get('benefit_description')

    benefit = Benefit(
      benefit_id = benefit_id,
      employee_id = employee_id,
      benefit_type = benefit_type,
      benefit_amount = benefit_amount,
      benefit_description = benefit_description
    )
    benefit.save()
    
    if benefit.pk:
      result = {
        'status': 'success',
        'message': 'Benefit saved',
        'benefit_id': benefit.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status': 'error',
        'message': 'Error saving benefit'
      }
  elif request.method == 'GET':
    return render(request, 'benefit/save_benefit.html', {})
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])

@csrf_exempt
def update_benefit(request):
  if request.method == 'PUT':
    benefit_id = request.POST.get('benefit_id')
    employee_id = request.POST.get('employee_id')
    benefit_type = request.POST.get('benefit_type')
    benefit_amount = request.POST.get('benefit_amount')
    benefit_description = request.POST.get('benefit_description')

    benefit = Benefit(
      benefit_id = benefit_id,
      employee_id = employee_id,
      benefit_type = benefit_type,
      benefit_amount = benefit_amount,
      benefit_description = benefit_description
    )
    benefit.save()
    if benefit.pk:
      result = {
        'status': 'success',
        'message': 'Benefit updated',
        'benefit_id': benefit.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status': 'error',
        'message': 'Error updating benefit'
      }
      return JsonResponse(result, status=500)
  elif request.method == 'GET':
    return render(request, 'benefit/update_benefit.html', {})
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])