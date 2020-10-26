from django.contrib import admin
from django.urls import path, include

# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('akun.urls')),
    path('', include('absensi_apps.urls', namespace='absensi')),
]
