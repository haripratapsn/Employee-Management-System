from django import forms
from .models import Employee,Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields=['dname','d_location']
        labels={'dname':"Department Name",'d_location':"Department Location"}
        widgets={
            'dname':forms.TextInput(attrs={'class':'form-control'}),
            'd_location':forms.TextInput(attrs={'class':'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['ename','age','salary','email','address','joining_date','dept']
        labels={
            'ename':'Employee Name',
            'age':'Age',
            'salary':'Salary',
            'email':'Email',
            'address':'Address',
            'joining_date':'Joining Date',
            'dept':'Department'
        }
        widgets={
            'ename':forms.TextInput(attrs={'type':'text',"class":"form-control"}),
            'age':forms.TextInput(attrs={"type":'number',"class":"form-control"}),
            'salary':forms.TextInput(attrs={"type":'number',"class":"form-control"}),
            'email':forms.EmailInput(attrs={'type':'email',"class":"form-control"}),
            'address':forms.Textarea(attrs={'cols':25,'rows':5,'placeholder':'Enter your address here',"class":"form-control"}),
            'joining_date':forms.DateInput(attrs={'type':'date',"class":"form-control"}),
            'dept':forms.Select(attrs={'class':'form-select','placeholder':'Select a Department'})
            
        }
