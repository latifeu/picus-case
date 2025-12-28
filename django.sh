#!/bin/bash
echo "Create migrations"
python manage.py makemigrations djangoapp
echo "------------------------------------"

echo  "Migrate"
python manage.py migrate
echo "------------------------------------"
chmod +x django.sh
echo "Start the server"
python manage.py runserver 0.0.0.0:8000


