#!/bin/sh

python manage.py makemigrations
python manage.py makemigrations core
python manage.py makemigrations scraper
python manage.py migrate
python manage.py migrate core
python manage.py migrate scraper

# Create superuser if it doesn't exist
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or \
User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell

# Run the server
exec "$@"
