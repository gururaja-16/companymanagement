from .models import Company, Employee, Department, Role, Attendance, LeaveRequest
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_info', 'logo']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'company', 'department', 'role', 'joining_date', 'salary']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['company', 'name']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['company', 'name']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'clock_in', 'clock_out']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'start_date', 'end_date', 'reason', 'approved']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']