import django.forms.fields
from django.shortcuts import render
from .forms import PostForm
from .models import Documents
from django.urls import reverse
from django.forms.fields import Field
from django.contrib.auth.models import User
from employees.models import Employee
from django.views.generic import (
    CreateView,
    DeleteView,
)
# Create your views here.

class UploadDocuments(CreateView):
    model = Documents
    template_name='documents/upload-file.html'
    fields= ['description', 'archive'] #'__all__'
    success_url = 'sucess/'

    def post(self, request, owner_id):
        form = super(UploadDocuments, self).get_form()
        form.instance.owner_id = owner_id
        if form.is_valid():
            return super(UploadDocuments, self).form_valid(form)
        else:
            return super(UploadDocuments, self).form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(UploadDocuments, self).get_context_data()
        user_ =  Employee.objects.filter(id=self.kwargs['owner_id'])
        context.update({'documents': user_})
        return context

    def get_success_url(self):
        return reverse('list_employees', kwargs={'pk':self.kwargs['owner_id']})

class DeleteDocuments(DeleteView):
    template_name='documents/upload-file.html'
    model = Documents