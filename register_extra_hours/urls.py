from django.urls import path, include
from .views import ListHours, editHours

urlpatterns = [
    path('', ListHours.as_view(), name='list_hours'), 
    path('edit/<int:pk>', editHours.as_view(), name='edit_hours'),
]
