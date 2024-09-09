from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CompanyViewSet, EmployeeViewSet, DepartmentViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
