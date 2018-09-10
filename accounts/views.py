from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
User = get_user_model()

def redirect_to_login(request):
    return redirect("/login")

def register_user(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        new_user=User.objects.create_user(username,email,password)
        return redirect("/login")

    return render(request,'accounts/register.html',context)

def login_user(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("/judge")
            else:
                return redirect("/contest")
        else:
            context['form']=LoginForm()
            context['error']="Invalid credentials."
    return render(request,'accounts/login.html',context)    