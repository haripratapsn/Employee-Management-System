from django.urls import path
from . import views 

urlpatterns=[
    #Dashboard
    path('',views.dashboaard_view,name='dashboard'),

    #Department
    path('create-department',views.create_department_view,name='create-department'),
    path('department-list',views.department_list_view,name='department-list'),
    path('update-department/<int:pk>',views.update_department_view,name="update-department"),
    path('delete-department/<int:pk>',views.delete_department_view,name="delete-department"),


    #Employee
    path('create-employee',views.create_employee_view,name='create-employee'),
    path('employee-list',views.employee_list_view,name='employee-list'),
    path('update-employee/<int:pk>',views.update_employee_view,name='update-employee'),
    path('delete-employee/<int:pk>',views.delete_employee_view,name='delete-employee'),
]