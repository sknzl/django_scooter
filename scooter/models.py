from django.db import models
from .helpers import haversine

# Create your models here.
class Scooter(models.Model):
    scooter_id = models.CharField(unique=True, max_length=255)
    last_lat = models.DecimalField(max_digits=9, decimal_places=6)
    last_lng = models.DecimalField(max_digits=9, decimal_places=6)
    distance_travelled = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scooter_id

class ScooterActivity(models.Model):
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def update_distance_travelled(self):
        distance = haversine(self.lng, self.lat, self.scooter.last_lng, self.scooter.last_lat)
        self.scooter.distance_travelled += distance
        self.scooter.last_lng = self.lng
        self.scooter.last_lat = self.lat
        self.scooter.save()
        print("Updated distance existing scooter")

    def __str__(self):
        return self.created.strftime("%d/%m/%Y, %H:%M:%S")


