import os

DEBUG = True


name = os.environ.get("DATABASE_NAME")
user = os.environ.get("DATABASE_USER")
password = os.environ.get("DATABASE_PASSWORD")
host = os.environ.get("DATABASE_HOST")
port = os.environ.get("DATABASE_PORT")


DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": name,
        "USER": user,
        "PASSWORD": password,
        "HOST": host,
        "PORT": port,
        }
    }
