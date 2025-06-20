from django import forms
from accounts.models import CustomUser  # или откуда ты берёшь юзера

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
