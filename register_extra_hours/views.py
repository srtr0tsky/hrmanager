from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView)
from .models import RegisterExtraHours

# Create your views here.
class ListHours(ListView):
    model = RegisterExtraHours
    template_name = 'register_hours/index.html'

    def get_queryset(self):
        enterprise_logged = self.request.user.employee.enterprise.id
        return RegisterExtraHours.objects.filter(employee__enterprise=enterprise_logged)
    

class editHours(UpdateView):
    model = RegisterExtraHours
    template_name = 'register_hours/edit_hours.html'
    fields = ['reason', 'hours']
    success_url = reverse_lazy('list_hours')
    def get_form(self):
        form = super().get_form(form_class=None)
        form.instance.employee_id = self.request.user
        return form
    