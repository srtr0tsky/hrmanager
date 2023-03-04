from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Department
from enterprise.models import Enterprise
from django import forms 
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
# Create your views here.

class DepartmentList(ListView):
    model = Department
    template_name= 'department/departments-index.html'
    
    fields = "__all__"
    def get_queryset(self):
        enterprise_id = self.request.user.employee.enterprise
        return Department.objects.filter(enterprise=enterprise_id)
    
class DepartmentUpdate(UpdateView):
    model = Department
    template_name= 'department/departments-update.html'
    fields = ['name', 'enterprise']
    def get_form(self): 
        form = super(DepartmentUpdate, self).get_form(form_class=None)
        form.fields['name'].label = "Department's name"
        return form
    def get_success_url(self):
        return reverse_lazy(f'list_departments') 
    
    def get_context_data(self):
        context = super().get_context_data()
        context.update({'pk': self.kwargs['pk']})
        return context
class DeleteDepartment(DeleteView):
    model = Department
    template_name = 'department/department-delete.html'
    def get(self, request, pk):
        Department.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/departments/')


class NewDepartment(CreateView):
    model = Department
    template_name = 'department/create_department.html'
    success_url = reverse_lazy('list_departments')
    fields= ['name']

    def form_valid(self, form):
        department = form.save(commit=False)
        department.enterprise = self.request.user.employee.enterprise
        department.save()
        return super(NewDepartment, self).form_valid(form)