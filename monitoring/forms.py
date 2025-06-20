from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")
