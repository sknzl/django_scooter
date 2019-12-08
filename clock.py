import os
import sys
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_scooter.settings')

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, "django_scooter"))
django.setup()

from services.get_scooters import get_scooters

get_scooters()

