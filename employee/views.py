from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeCreationForm, EmployeeUpdateForm
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

class EmployeeCreateView(CreateView):
  model = Employee
  form_class = EmployeeCreationForm
  template_name = 'templates/employee/create.html'
  success_url = reverse_lazy('employee:list')

class EmployeeUpdateView(UpdateView):
  model = Employee
  form_class = EmployeeUpdateForm
  template_name = 'templates/employee/update.html'
  success_url = reverse_lazy('employee:list')

@csrf_exempt
def post_employee(request):
  if request.method == 'POST':
    employee_id = request.POST.get('employee_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    department = request.POST.get('department')
    position = request.POST.get('position')
    hire_date = request.POST.get('hire_date')

    employee = Employee(
      employee_id=employee_id,
      first_name=first_name,
      last_name=last_name,
      date_of_birth=date_of_birth,
      gender=gender,
      address=address,
      email=email,
      phone=phone,
      department=department,
      position=position,
      hire_date=hire_date
    )

    employee.save()

    if employee.pk:
      result = {
        'status': 'success',
        'message': 'Employee created successfully',
        'employee_id': employee.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status':'error',
        'message': 'Employee creation failed'
      }
      return JsonResponse(result, status=400)
  elif request.method == 'GET':
    return render(request, 'templates/employee/create.html')
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])

@csrf_exempt
def put_employee(request):
  if request.method == 'PUT':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    date_of_birth = request.POST.get('date_of_birth')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    department = request.POST.get('department')
    position = request.POST.get('position')
    hire_date = request.POST.get('hire_date')

    employee = Employee(
      first_name=first_name,
      last_name=last_name,
      date_of_birth=date_of_birth,
      gender=gender,
      address=address,
      email=email,
      phone=phone,
      department=department,
      position=position,
      hire_date=hire_date
    )
    employee.update()

    if employee.pk:
      result = {
        'status': 'success',
        'message': 'Employee updated successfully',
        'employee_id': employee.pk
      }
      return JsonResponse(result, status=301)
    else:
      result = {
        'status': 'error',
        'message': 'Employee update failed'
      }
      return JsonResponse(result, status=500)
  elif request.method == 'GET':
    return render(request, 'templates/employee/update.html')
  else:
    return HttpResponseNotAllowed(['PUT', 'GET'])