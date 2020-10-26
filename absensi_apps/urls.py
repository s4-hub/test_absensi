from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'absensi'

# router = routers.DefaultRouter()
# router.register('api', views.ScanViewSet, basename='api')

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('absen/', views.scan_absen, name='absen'),
    path('api/', views.apiOverview),
    path('api/list/', views.scanList),
    path('api/detail/<str:pk>', views.scanDetail),
    path('api/scan', views.scanCreate),
    path('absen/list', views.list_absen, name='list'),
    # path('logout/', views.singout, name='logout'),
]
