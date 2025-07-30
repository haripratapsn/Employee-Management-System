from django.urls import path
from . import views

urlpatterns=[
    path('create/employee-profile/<int:pk>',views.create_employee_profile_view,name="create-employee-profile"),
    path('update/employee-profile/<int:pk>',views.update_employee_profile_view,name="update-employee-profile"),
    path('delete/employee-profile/<int:pk>',views.delete_profile_view,name="delete-employee-profile"),
    path('view/<int:pk>',views.profile_view,name='profile')
    
]