#!/bin/bash
python manage.py migrate
gunicorn DjangoProject.wsgi:application --bind 0.0.0.0:8000