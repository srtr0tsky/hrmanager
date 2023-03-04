from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Enterprise
# Create your views here.

class CreateEnterprise(CreateView):
    model = Enterprise
    fields = ['name']
    success_url = '/sucess'
    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.enterprise = obj
        employee.save()
        return HttpResponse("Deu bom")
    
class EditEnterprise(UpdateView): 
    model = Enterprise
    fields = ['name']
    success_url = '/'