from django.urls import path, include
from .views import UploadDocuments, DeleteDocuments
urlpatterns = [
    path('x/<int:owner_id>', UploadDocuments.as_view(), name="upload_documents" ),
    path('delete/<int:pk>', DeleteDocuments.as_view(), name="delete_documents")
]
