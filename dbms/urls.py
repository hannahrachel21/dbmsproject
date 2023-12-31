from django.urls import path
from .views import employee_list, delete_employee, update_employee,update_employee_confirm
from .views import members_list, delete_members, update_members,update_members_confirm
from .views import adminsucess

urlpatterns = [
    path('', adminsucess, name='adminsucess'),
    path('employee_list/', employee_list, name='employee_list'),
    path('delete_employee/', delete_employee, name='delete_employee'),
    path('update_employee/<int:employee_id>/', update_employee, name='update_employee'),
    path('update_employee/<int:employee_id>/confirm/', update_employee_confirm, name='update_employee_confirm'),
    path('members_list/', members_list, name='members_list'),
    path('delete_members/', delete_members, name='delete_members'),
    path('update_members/<int:members_id>/', update_members, name='update_members'),
    path('update_members/<int:members_id>/confirm/', update_members_confirm, name='update_members_confirm'),
    path('adminsucess/', adminsucess, name='adminsucess'),
    ]
