from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import DeleteView,UpdateView,TemplateView,ListView,DetailView,CreateView
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'

class EmployeeList(ListView):
    model = Employee
    context_object_name='employees'

class EmployeeDetail(DetailView):
    model=Employee
    context_object_name='empobject'

class EmployeeCreate(CreateView):
    model=Employee
    fields='__all__'

class EmployeeUpdate(UpdateView):
    model=Employee
    fields='__all__'

class Employeedelete(DeleteView):
    model=Employee
    context_object_name='Employeeobject'
    success_url=reverse_lazy('EmployeeList')