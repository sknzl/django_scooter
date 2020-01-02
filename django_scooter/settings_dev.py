# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django_scooter_3",
        "USER": "postgres"
    }
}
