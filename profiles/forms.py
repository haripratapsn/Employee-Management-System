from django import forms
from .models import EmployeeProfile

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model=EmployeeProfile
        fields=['image','resume','phone_no','linkedin','bio']
        labels={'image':'Profile Picture',}
        widgets={
            'bio':forms.Textarea(attrs={'class':"form-control form-control-sm",'cols':25,'rows':5,'placeholder':'Enter your bio here'}),
            'image':forms.FileInput(attrs={'type':'file','class':"form-control form-control-sm",'name':"image" }),
            'resume':forms.FileInput(attrs={'name':'resume','type':'file','class':"form-control form-control-sm",'accept': '.pdf,.doc,.docx' }),
            'linkedin':forms.URLInput(attrs={'type':'url','class':"form-control form-control-sm",'placeholder': 'https://www.linkedin.com/in/your-profile' }),
            'phone_no':forms.TextInput(attrs={'type':'tel','class':"form-control form-control-sm",'value':'+91 ' }),
        }