
from django.urls import path
from .views import core_page

urlpatterns = [
    path('', core_page, name='home_page'),
]
