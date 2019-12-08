# Django Scooter
Project related to the article in my [blog](https://sknzl.github.io/tracking-electric-scooters-in-lisbon/)

# How to use
- PostgreSQL must be running with a created database called `scooter_db`.
- Redis must be running.
- Clone the repository.
- Create a python3 venv, activate it, and install the required packages with `pip install -r requirements.txt`.
- Run `python manage.py migrate` to apply database migrations.
- Create a django admin user `python manage.py createsuperuser`.
- Set the environment variables `GOOGLE_MAPS_API_KEY` and `FLASH_DEVICE_KEY`
- Start the django dev server with `python manage.py runserver`
- Start celery with `celery -A app.celery  worker --loglevel=info -B`
- Go to http://localhost:8000/admin and check the scooter model after the celery task was runnin a few times.

