from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически логиним после регистрации
            return redirect('home')  # перенаправим на главную
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
