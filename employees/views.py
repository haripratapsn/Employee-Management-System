from django.shortcuts import render,redirect,get_object_or_404
from .forms import DepartmentForm,EmployeeForm
from .models import Department,Employee

# Create your views here.
#Dashboard---------------------------------------------
def dashboaard_view(request):
    emp_count=Employee.objects.count()
    dept_count=Department.objects.count()
    context={
        'emp_count':emp_count,
        'dept_count':dept_count
    }
    return render(request,'dashboard.html',context)

#Department--------------------------------------------
def create_department_view(request):
    context={}
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            context['error']='Invalid Data'
    form=DepartmentForm()
    context={
        'form':form
    }
    return render(request,'create_department.html',context)

def department_list_view(request):
    departments=Department.objects.all()
    context={
        'departments':departments
    }
    return render(request,'department_list.html',context)

def update_department_view(request,pk):
    dept=get_object_or_404(Department,id=pk)

    if request.method=="POST":
        form=DepartmentForm(request.POST,instance=dept)
        if form.is_valid():
            form.save()
            return redirect("department-list")
    form=DepartmentForm(instance=dept)
    context={
        'form':form
    }
    return render(request,'update_department.html',context)

def delete_department_view(request,pk):
    dept=get_object_or_404(Department,id=pk)
    dept.delete()
    return redirect('department-list')

#Employee------------------------------------------------------------------

def create_employee_view(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee-list')
    form=EmployeeForm()
    context={
        'form':form
    }
    return render(request,'create_employee.html',context)


def employee_list_view(request):
    employees=Employee.objects.all()
    context={
        "employees":employees,
    }
    return render(request,"employee_list.html",context)

def update_employee_view(request,pk):
    employee=get_object_or_404(Employee,id=pk)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    form=EmployeeForm(instance=employee)
    context={
        'form':form
    }
    return render(request,'update_employee.html',context)


def delete_employee_view(request,pk):
    employee=get_object_or_404(Employee,id=pk)
    employee.delete()
    return redirect('employee-list')


