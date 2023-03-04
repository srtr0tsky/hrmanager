from django.db import models
from django.contrib.auth.models import User
from department.models import Department
from enterprise.models import Enterprise


class Employee(models.Model):

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ManyToManyField(Department)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name