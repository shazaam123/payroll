from django.shortcuts import render
from .models import Payroll
from django.http import JsonResponse, HttpResponseNotAllowed
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_payroll(request):
  if request.method == 'POST':
    employee_id = request.POST.get('employee_id')
    pay_date = datetime.strptime(request.POST.get('pay_date'), '%Y-%m-%d')
    gross_salary = request.POST.get('gross_salary')
    net_salary = request.POST.get('net_salary')
    pay_method = request.POST.get('pay_method')

    if pay_method == 'standard':
      net_salary = gross_salary * 0.9
    elif pay_method == 'overtime':
      net_salary = gross_salary * 0.85
    elif pay_method == 'commission':
      net_salary = gross_salary * 0.95

    if gross_salary < 2350000:
      nssf = gross_salary * 0.05
      E_Cont = gross_salary * 0.1
      paye1 = 0
      gratuity = float(gross_salary * 0.3)
      deductions = nssf + paye1
      net_salary = gross_salary - deductions
      
      
    
    payroll = Payroll(
      employee_id=employee_id,
      pay_date=pay_date,
      gross_salary=gross_salary,
      net_salary=net_salary,
      pay_method=pay_method
    )

    payroll.save()

    if payroll.pk:
      result = {
        'status': 'success',
        'message': 'Payroll saved successfully',
        'employee_id': employee_id.pk
      }
      return JsonResponse(result, status=201)
    else:
      result = {
        'status':'error',
        'message': 'Error in saving Payroll'
      }
  elif request.method == 'GET':
    return render(request, 'templates/save_payroll.html', {})
  else:
    return HttpResponseNotAllowed(['POST', 'GET'])