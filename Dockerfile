FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Создаём суперюзера admin/adminpass, если он ещё не существует
CMD ["sh", "-c", "python manage.py migrate && echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')\" | python manage.py shell && python manage.py runserver 0.0.0.0:8000"]
