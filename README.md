# Django Scooter
Project related to the article in my [blog](https://sknzl.github.io/posts/tracking-electric-scooters-in-lisbon/)

# How to use local
- PostgreSQL must be running with a created database called `scooter_db`.
- Redis must be running.
- Clone the repository.
- Create a python3 venv, activate it, and install the required packages with `pip install -r requirements.txt`.
- Run `python manage.py migrate` to apply database migrations.
- Create a django admin user `python manage.py createsuperuser`.
- Set the environment variables `GOOGLE_MAPS_API_KEY` and `FLASH_DEVICE_KEY`
- Start the django dev server with `python manage.py runserver`
- Start celery with `celery -A app.celery  worker --loglevel=info -B`
- Go to http://localhost:8000/admin and check the scooter model after the celery task was running a few times.

# Use with Docker
Dockerfile is configured to run Django and Celery in the same container.

# Development and Production environment
If the environment variables `PRODUCTION` is set (any value) then `settings_production.py` is loaded instead of `settings_dev.py`.

# Recorded data
The data-set recorded from 19th August 2019 to 8th December 2019 is available [here](https://github.com/sknzl/django_scooter_data)