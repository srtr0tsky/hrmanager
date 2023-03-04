from django import forms as FORMS
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView)

from .models import Employee
import uuid
# Create your views here.



def employees_page(request):
    return HttpResponse('Hello')

class listEmployee(ListView):
    model = Employee
    template_name='employees/employees_list.html'

    def get_queryset(self):
        enterprise_logged_in = self.request.user.employee.enterprise
        return Employee.objects.filter(enterprise=enterprise_logged_in)

class editEmployee(UpdateView):
    model = Employee
    template_name= 'employees/employee_edit.html'
    fields = ['name', 'department']
    success_url = 'sucess/'
    def get_form(self, form_class=None):
        forms = super().get_form(form_class)
        forms.fields['name'].label = 'Edit Employee name'
        return forms
    def get_context_data(self):          
        context = super(editEmployee, self).get_context_data()
        context.update({
            'user_n': self.request.user.employee.name, 
            'resume_pk': self.kwargs['pk'],
            })
        return context

class DeleteEmployee(DeleteView):
    model = Employee
    template_name='employees/delete_employee.html'
    def get(self, request, pk):
        employee_id = self.kwargs['pk']
        Employee.objects.filter(id=employee_id).delete()
        return HttpResponseRedirect('/employees/')
class CreateEmployee(CreateView):
    model = Employee
    template_name= 'employees/create_employee.html'
    fields= ['name', 'department']
    def get_form(self, form_class=None):
        forms = super().get_form(form_class)
        forms.fields['name'].widget = FORMS.TextInput({'placeholder': "Type employee's name..."})
        forms.fields['name'].label = "Employee's name"
        return forms
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.enterprise = self.request.user.employee.enterprise
        form.user = User.objects.create(
            username=uuid.uuid4().hex, 
            password=self.request.user.password)
        form.save()
        return HttpResponseRedirect('/employees/')