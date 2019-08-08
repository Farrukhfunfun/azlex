from django.shortcuts import render
from .models import Education, Employee

def engmainpage(request):
    employee = Employee.objects.all()
    for emp in employee:
        print(emp.photo)
    return render(request, 'engmain/engmain.html', {'employee': employee})
