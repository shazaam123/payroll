from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from ..models import Employee
from django.http import JsonResponse

@api_view(['POST'])
def employee_create(request):
  data = request.data

  existing_employee = Employee.objects.filter(first_name=data['first_name'], last_name=data['last_name']).first()

  if existing_employee:
    serializers = EmployeeSerializer(existing_employee)
    return Response(serializers.data, status=200)
  else:
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def employee_update(request, pk):
  if request.method == 'GET':
    employee = Employee.objects.get(employee_id=pk)
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == 'PUT':
    data = request.data
    employee = Employee.objects.get(employee_id=pk)
    serializer = EmployeeSerializer(instance=employee, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=400)
  else:
    return Response("Invalid request method", status=405)