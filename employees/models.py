from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=50)
    d_location=models.CharField(max_length=30)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    ename=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.FloatField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    joining_date=models.DateField(null=True,blank=True)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
  

    def __str__(self):
        return self.ename
    

