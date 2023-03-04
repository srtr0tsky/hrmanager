from django.urls import path
from .views import (
    DepartmentList, 
    DepartmentUpdate,
    NewDepartment,
    DeleteDepartment, 
    )
urlpatterns = [
    path('', DepartmentList.as_view(), name='list_departments'),
    path('update/<int:pk>', DepartmentUpdate.as_view(), name='update_department'),
    path('new', NewDepartment.as_view(), name='new_department'),
    path('delete/<int:pk>', DeleteDepartment.as_view(), name='delete_department'),
]
