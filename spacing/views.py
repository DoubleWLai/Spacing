from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

from .models import memory

def index(request):
    if request.user.is_authenticated:
        Userdata = memory.objects.filter(user=request.user)
        l = []
        for i in Userdata:
            m = i.content
            l.append(m)
        context = {"content" : l}
        return render(request, 'spacing/index.html',context)
    else:
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
    if request.user.is_authenticated:
        if request.method == "POST":
            content = request.POST['content']
            user = request.user
            newMemory = memory.objects.create(user=user, content=content)
            return render(request, 'spacing/create.html')
        else:
            return render(request, 'spacing/create.html')
    else:
        return redirect('/login')

def list(request):
    if request.user.is_authenticated:
        Userdata = memory.objects.filter(user=request.user)
        l = []
        for i in Userdata:
            l.append(i)
        context = {"list" : l}
        return render(request, 'spacing/list.html',context)
    else:
        return redirect("/login")

def list_delete(request,id):
    delete_item = memory.objects.filter(id=id)
    delete_item.delete()
    return redirect("/list")
