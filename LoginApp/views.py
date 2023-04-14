from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    return render(request,'log.html')

def reg(request):
    return render(request,'reg.html')

def read_reg(request):
    un = request.POST['t1']
    em = request.POST['t2']
    ps = request.POST['t3']
    U= User.objects.create_superuser(un,em,ps)
    U.save()
    return render(request,'log.html',{'msg':un,'user':'User Name: '})


def read_log(request):
    un = request.POST['t1']
    ps = request.POST['t2']
    A = authenticate(username=un,password=ps)
    if A is not None:
        login(request,A)
        return render(request,'index.html',{'A':un.upper()})
    else:
        return render(request,'log.html')


def read_logout(request):
    logout(request)
    return render(request,'logout.html')
