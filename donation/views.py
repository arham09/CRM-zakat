from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context ={
        "form": login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username  = login_form.cleaned_data.get("username")
        password  = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/index")
        else:
            print("Error")

    return render(request, "auth/login.html", context)

def index(request):
    return render(request, 'index.html', {})
    
