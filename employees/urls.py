from django.urls import path, include
from .views import listEmployee, editEmployee, DeleteEmployee, CreateEmployee
urlpatterns = [
    path('', listEmployee.as_view() , name='list_employees'),
    path("edit_employee/<int:pk>", editEmployee.as_view() , name="edit_employee"),
    path('delete/<int:pk>', DeleteEmployee.as_view(), name='delete_employee'),
    path('create/', CreateEmployee.as_view(), name='create_employee'),
]
