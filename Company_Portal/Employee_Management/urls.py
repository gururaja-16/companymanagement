"""
URL configuration for Employee_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('myapp.urls')),
    path('api/', include('myapp.api_urls')),
    path('Index', views.Index, name='Index'),
    path('base', views.base, name= 'base'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_register', views.user_register, name='user_register'),
    path('company_list', views.company_list, name='company_list'),
    path('create_company', views.create_company, name='create_company'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('role_list', views.role_list, name='role_list'),
    path('department_list', views.department_list, name='department_list'),
    path('create_employee', views.create_employee, name='create_employee'),
    path('create_department', views.create_department, name='create_department'),
    path('create_role',views.create_role, name='create_role'),
    path('employee/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('Leave_request', views.Leave_request, name='Leave_request'),
    path('company/<int:pk>/update/', views.update_company, name='update_company'),
    path('company/<int:pk>/delete/', views.delete_company, name='delete_company'),
    path('department/<int:pk>/edit/', views.update_department, name='update_department'),
    path('department/<int:pk>/delete/', views.delete_department, name='delete_department'),
    path('role/update/<int:pk>/', views.update_role, name='update_role'),
    path('role/delete/<int:pk>/', views.delete_role, name='delete_role'),
    path('doctdisplay', views.displayfunction, name='doctdisplay'),
    path('departdis', views.displayfunction2, name='departdis'),

]

