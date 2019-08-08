from django.shortcuts import render
from .models import Education, Employee

def mainpage(request):
    employee = Employee.objects.all()
    return render(request, 'main/main.html', {'employee': employee})
