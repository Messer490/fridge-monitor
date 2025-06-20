from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('analytics/', views.analytics_view, name='analytics'),
    path('analytics/export/', views.export_csv, name='export_csv'),
    path('map/', views.map_view, name='map'),
    path('', views.home_view, name='home'),
    path('api/temperature/', views.receive_temperature, name='receive_temperature'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # наше новое
]
