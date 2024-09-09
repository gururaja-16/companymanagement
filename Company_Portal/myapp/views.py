from django.shortcuts import get_object_or_404
from .models import Company, Employee, Department
from .forms import EmployeeForm, CompanyForm, DepartmentForm, LeaveRequestForm, AttendanceForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Role
from .forms import RoleForm

def Index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Index')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Example view to list companies
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'roles_list.html', {'roles': roles})

# Example view to create a new company
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form1 = EmployeeForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('employee_list')
    else:
        form1 = EmployeeForm()
    return render(request, 'create_employee.html',{'form1': form1})

def create_department(request):
    if request.method == 'POST':
        form2 = DepartmentForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('department_list')
    else:
        form2 = DepartmentForm()
    return render(request, 'create_department.html',{'form2': form2})

def create_role(request):
    if request.method == 'POST':
        form3 = RoleForm(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            return redirect('role_list')
    else:
        form3 = RoleForm()
    return render(request,'create_role.html',{'form3': form3})

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})


def department_list(request):
    departments = Department.objects.all()
    return render(request,'department_list.html', {'departments' : departments})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect or render a success page
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'confirm_delete.html', {'employee': employee})

def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'update_company.html', {'form': form, 'company': company})

def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'confirm_delete.html', {'company': company})

def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('department_list')
    return render(request, 'confirm_delete.html', {'department': department})

def update_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'update_role.html', {'form': form, 'role': role})

def delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'confirm_delete.html', {'role': role})

def Leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Leave_request')
    else:
        form = LeaveRequestForm()
    return render(request,'Leave_request.html',{'form': form})

def Attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Attendance')
    else:
        form = AttendanceForm()
    return render(request,'Attendance.html',{'form': form})

def displayfunction(request):
    s1=Company.objects.all()
    dict1={'company':s1}
    return render(request,'company.html',dict1)

def displayfunction2(request):
    s2=Department.objects.all()
    dict2={'department':s2}
    return render(request,'department.html',dict2)