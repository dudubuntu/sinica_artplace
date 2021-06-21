#! /bin/bash

python manage.py makemigrations --no-input

python manage.py makemigrations api --no-input

python manage.py makemigrations contactus --no-input

python manage.py migrate --no-input

python manage.py migrate api --no-input

python manage.py migrate contactus --no-input

python manage.py collectstatic --no-input

python manage.py createsuperuser --no-input

exec gunicorn sinica_proj.wsgi:application -b 0.0.0.0:8000 --reload