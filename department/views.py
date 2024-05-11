from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Department
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_department(request):
  if request.method == 'POST':
    
    deparment_id = request.POST.get('department_id')
    department_name = request.POST.get('department_name')
    
    department = Department(
      department_name = department_name
    )
    
    department.save()
    
    if department.pk:
      result = {
        'status':'success',
        'message':'Department saved successfully',
        'department_id':department.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status': 'error',
        'message': 'Department not saved'
      }
      return JsonResponse(result, status=400)
  elif request.method == 'GET':
    return render(request, 'template/department.html')
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])
  