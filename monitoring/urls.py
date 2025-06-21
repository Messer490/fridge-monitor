from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
# urls.py
from django.urls import path
from .views import admin_dashboard
from .views import admin_dashboard

urlpatterns = [
    path('analytics/', views.analytics_view, name='analytics'),
    path('analytics/export/', views.export_csv, name='export_csv'),
    path('map/', views.map_view, name='map'),
    path('', views.home_view, name='home'),
    path('api/temperature/', views.receive_temperature, name='receive_temperature'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # наше новое
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),

]
