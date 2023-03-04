from django.urls import path, include
from .views import CreateEnterprise, EditEnterprise
urlpatterns = [
    path('new/', CreateEnterprise.as_view(), name="create_enterprise" ),
    path('edit/<int:pk>', EditEnterprise.as_view(), name="edit_enterprise")
]
