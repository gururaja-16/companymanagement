from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    contact_info = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='roles')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees')
    joining_date = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)
