from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # если ты используешь кастомного юзера

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # замени на User, если не кастомный
        fields = ['username', 'email', 'password1', 'password2']