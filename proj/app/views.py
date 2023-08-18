from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Employee , Role , Department
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'home.html')


def emp_all(request):
    gets = Employee.objects.all()
    return render(request,'emp_all.html',{'gets':gets})


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phome=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return redirect('/')
    else:
        return render(request,'add_emp.html')


def remove_emp(request,ids):
    gets = Employee.objects.filter(id=ids)
    gets.delete()
    return redirect('emp_all')


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        gets = Employee.objects.all()
        if name:
            gets = gets.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        
        context = {
            'gets': gets
        }
        return render(request,'emp_all.html',context)

    else:
        return render(request,'home.html')


