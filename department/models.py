from django.db import models
from enterprise.models import Enterprise
class Department(models.Model):
    name = models.CharField(max_length=100)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)

    def __str__(self):
        return self.name