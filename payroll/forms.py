from django import forms
from payroll.models import Employee, SalaryDetail, TaxDetail, Benefit, Attendance, PayrollHistory, User, Announcement
from payroll.models import Department 

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class SalaryDetailForm(forms.ModelForm):
    class Meta:
        model = SalaryDetail
        fields = '__all__'

class TaxDetailForm(forms.ModelForm):
    class Meta:
        model = TaxDetail
        fields = '__all__'

class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class PayrollHistoryForm(forms.ModelForm):
    class Meta:
        model = PayrollHistory
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
