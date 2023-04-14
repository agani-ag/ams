from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from poApp.models import City, Course, Student
from django.http import HttpResponse

# Create your views here.
@login_required
def insert(request):
    c1=City.objects.all()
    c2=Course.objects.all()
    x={'c1':c1, 'c2':c2}
    return render(request,'insert.html',x)

def insert_data(request):
    b1=Student()
    b1.fname = request.POST["t1"]
    b1.lname = request.POST["t2"]
    b1.mobile = request.POST["t3"]
    b1.email = request.POST["t4"]
    b1.city = City.objects.get(city_n=request.POST["t5"])
    b1.course = Course.objects.get(course_n=request.POST["t6"])
    b1.save()
    x=request.POST["t1"]+' '+request.POST["t2"]

    return render(request,'thanks.html',{'A':x.upper()})

@login_required
def display_fun(request):
    b1 = Student.objects.all()
    return render(request,'display.html',{'data':b1})

@login_required
def update_fun(request,id):
    c1 = City.objects.all()
    c2 = Course.objects.all()
    b1 = Student.objects.get(id=id)
    x = {'c1': c1, 'c2': c2,'b1':b1}
    if request.method == 'POST':
        b1.fname = request.POST["t1"]
        b1.lname = request.POST["t2"]
        b1.mobile = request.POST["t3"]
        b1.email = request.POST["t4"]
        b1.city = City.objects.get(city_n=request.POST["t5"])
        b1.course = Course.objects.get(course_n=request.POST["t6"])
        b1.save()
        return redirect('display')

    return render(request,'update.html',x)

@login_required
def delete_fun(request,id):
    b1 = Student.objects.get(id=id)
    b1.delete()
    return redirect('display')


def navbar(request):
    return render(request,'navbar.html')

def index(request):
    return render(request,'index.html')
