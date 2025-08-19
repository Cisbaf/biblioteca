#!/bin/sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 1 --threads 2