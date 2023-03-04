from django.db import models
from django.urls import reverse
from employees.models import Employee


class Documents(models.Model):
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    archive = models.FileField(upload_to='documents/media/')
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse("list_employees")
    