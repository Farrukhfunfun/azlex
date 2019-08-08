from django.shortcuts import render
from .models import Education, Employee

def uzbmainpage(request):
    employee = Employee.objects.all()
    return render(request, 'uzbmain/uzbmain.html', {'employee': employee})
