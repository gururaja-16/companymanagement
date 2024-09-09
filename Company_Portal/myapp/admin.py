from django.contrib import admin
from .models import Company, Department, Role, Employee, Attendance, LeaveRequest

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
