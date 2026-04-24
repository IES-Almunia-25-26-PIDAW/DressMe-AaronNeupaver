#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn DjangoProject.wsgi:application --bind 0.0.0.0:8000