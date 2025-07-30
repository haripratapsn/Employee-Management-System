from django.shortcuts import render,redirect,get_object_or_404
from .forms import EmployeeProfileForm
from .models import EmployeeProfile
from employees.models import Employee

# Create your views here.
def create_employee_profile_view(request,pk):
    context={}
    employee=get_object_or_404(Employee,id=pk)
    
    if EmployeeProfile.objects.filter(employee=employee).exists():
        return redirect('profile',pk=employee.id)
    
    if request.method=="POST":
        form=EmployeeProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.employee=employee
            profile.save()
            return redirect('employee-list')
        else:
            context['error']='Somethin went wrong'
    form=EmployeeProfileForm(initial={'employee':employee.ename})
    context={
        'employee':employee,
        'form':form
    }
    return render(request,'create_employee_profile.html',context)




def update_employee_profile_view(request,pk):
    context={}
    employee=get_object_or_404(Employee,id=pk)
    employee_profile=get_object_or_404(EmployeeProfile,employee=employee)

    if request.method=="POST":
        form=EmployeeProfileForm(request.POST,request.FILES,instance=employee_profile)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('employee-list')
        else:
            context={
                'error':'something went wrong'
            }
    form=EmployeeProfileForm(instance=employee_profile,initial={'employee':employee.ename})
    context={
        'employee_profile':employee_profile,
        'employee':employee,
        'form':form
    }
    return render(request,'update_employee_profile.html',context)



        
def profile_view(request,pk):
    employee=get_object_or_404(Employee,id=pk)
    employee_profile=get_object_or_404(EmployeeProfile,employee=employee)

    context={
        'employee':employee,
        'employee_profile':employee_profile
    }

    return render(request,"profile.html",context)

def delete_profile_view(request,pk):
    employee_profile=get_object_or_404(EmployeeProfile,id=pk)
    employee_profile.delete()
    return redirect('employee-list')


