from django.db import models
from employees.models import Employee

class RegisterExtraHours(models.Model):
    reason = models.CharField(max_length=450)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, default=1)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.reason
    
