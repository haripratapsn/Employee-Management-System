from django.db import models
from employees.models import Employee

# Create your models here.
class EmployeeProfile(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
    bio=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    resume=models.FileField(upload_to='resumes',null=True,blank=True)
    linkedin=models.URLField(null=True,blank=True)
    phone_no=models.CharField(max_length=14)

    def __str__(self):
        return self.employee.ename
   

    

