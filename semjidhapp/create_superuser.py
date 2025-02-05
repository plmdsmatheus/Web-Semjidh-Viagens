import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semjidhapp.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Obtenha as informações do superusuário das variáveis de ambiente
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("Superusuário já existe.")
else:
    print("Variáveis de ambiente para superusuário não definidas.")
