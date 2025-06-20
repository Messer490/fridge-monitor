from django.shortcuts import render
from .models import Fridge, TemperatureReading
from django.utils import timezone
from datetime import timedelta
import csv
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import json
from .models import Store, Fridge
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from monitoring.models import Fridge, TemperatureReading, Notification
import json

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def analytics_view(request):
    fridges = Fridge.objects.all()
    selected_fridge = request.GET.get('fridge')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    readings = TemperatureReading.objects.all()

    if selected_fridge:
        readings = readings.filter(fridge_id=selected_fridge)

    if date_from:
        readings = readings.filter(timestamp__gte=date_from)
    if date_to:
        readings = readings.filter(timestamp__lte=date_to)

    context = {
        'fridges': fridges,
        'readings': readings.order_by('-timestamp')[:100],
    }
    return render(request, 'monitoring/analytics.html', context)


def export_csv(request):
    fridge_id = request.GET.get('fridge')
    readings = TemperatureReading.objects.filter(fridge_id=fridge_id) if fridge_id else TemperatureReading.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperature_readings.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fridge', 'Value', 'Timestamp'])
    for r in readings:
        writer.writerow([r.fridge.name, r.value, r.timestamp])

    return response

def map_view(request):
    stores_qs = Store.objects.prefetch_related('fridges').all()
    stores = []
    for store in stores_qs:
        stores.append({
            'name': store.name,
            'address': store.address,
            'latitude': store.latitude,
            'longitude': store.longitude,
            'fridges': [
                {
                    'name': fridge.name,
                    'current_temperature': fridge.current_temperature,
                    'temperature_min': fridge.temperature_min,
                    'temperature_max': fridge.temperature_max,
                } for fridge in store.fridges.all()
            ]
        })

    return render(request, 'monitoring/map.html', {'stores': json.dumps(stores, cls=DjangoJSONEncoder)})
def home_view(request):
    return render(request, 'monitoring/home.html')



@csrf_exempt
def receive_temperature(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/x-www-form-urlencoded':
                fridge_id = request.POST.get('fridge_id')
                value = request.POST.get('value')
            else:
                data = json.loads(request.body)
                fridge_id = data.get('fridge_id')
                value = data.get('value')

            fridge = Fridge.objects.get(id=fridge_id)
            value = float(value)

            TemperatureReading.objects.create(fridge=fridge, value=value)
            fridge.current_temperature = value
            fridge.save()

            # Проверка и уведомление
            if value < fridge.temperature_min or value > fridge.temperature_max:
                msg = f"⚠️ {fridge.name}: {value}°C (норма {fridge.temperature_min}–{fridge.temperature_max})"
                Notification.objects.create(fridge=fridge, message=msg)

            return JsonResponse({'status': 'success', 'message': 'Данные получены'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'error': 'POST only'}, status=405)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')  # или redirect('map') если хочешь
            return redirect('map')  # обычный пользователь
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = '/accounts/login/'

