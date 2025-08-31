from django.shortcuts import render

# Create your views here.
def signup_view(request):
    context={}

    return render(request,"signup.html",context)

def login_view(request):
    context={}
    return render(request,"login.html",context)
