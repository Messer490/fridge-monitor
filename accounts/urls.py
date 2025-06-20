from django.urls import path
from .views import register_view

from .views import register_view, login_view, logout_view, CustomPasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
]