from services.get_scooters import get_scooters
from celery.schedules import crontab
from celery.task import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(minutes=10))
def scooter_task():
    get_scooters()