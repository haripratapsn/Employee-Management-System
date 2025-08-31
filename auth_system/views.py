from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def signup_view(request):
    if request.method=="POST":
        data=request.POST
        form=UserCreationForm(data)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserCreationForm()

    context={"form":form}
    return render(request,"signup.html",context)

def login_view(request):
    if request.method=="POST":
        data=request.POST
        form=AuthenticationForm(data=data)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in data:
                return redirect(data.get('next'))
            else:
                return redirect("dashboard")
    else:
        form=AuthenticationForm()
    context={"form":form}

    return render(request,"login.html",context)

def logout_view(request):
    logout(request)
    return redirect("login")
