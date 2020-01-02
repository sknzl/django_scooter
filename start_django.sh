python manage.py collectstatic --noinput
python manage.py migrate
gunicorn django_scooter.wsgi --bind=0.0.0.0:8000 --timeout 120
