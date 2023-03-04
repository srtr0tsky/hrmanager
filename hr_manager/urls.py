from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls'), name='home'),
    path('employees/', include('employees.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('enterprises/', include('enterprise.urls')),
    path('departments/', include('department.urls')),
    path('documents/', include('documents.urls')),
    path('hours/', include('register_extra_hours.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)