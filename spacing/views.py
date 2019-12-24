from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

from .models import memory

def index(request):
    return render(request, 'spacing/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
        return redirect("/")
    else:
        form = RegisterForm()
    return render(request, 'spacing/register.html', {"form":form})

def create(request):
    return render(request, "spacing/create.html")
