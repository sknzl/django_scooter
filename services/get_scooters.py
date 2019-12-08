import math
import requests
import numpy as np
from scooter.models import Scooter, ScooterActivity
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def generate_gridpoints():
    gridpoints = []
    lat_start = 38.70
    lat_end = 38.75
    lng_start = -9.16
    lng_end = -9.11

    for x in np.linspace(lat_start, lat_end, num=10):
        for y in np.linspace(lng_start, lng_end, num=10):
            gridpoints.append({"lat":round(x, 4), "lng":round(y, 4)})
    return gridpoints

def get_bearer():
    url = "https://api.goflash.com/api/Mobile/UserHello?deviceKey={}&ownerName=django_scooter&deviceInfo1=django&deviceInfo2=scooter&osInfo1=python&osInfo2=3&appVersion=2.2.1 (647)&lang=en&translationDictionaryTimestamp=2019-07-30 16:50:57.833&cityAreasTimestamp=2019-07-31T11:13:07.64".format(settings.FLASH_DEVICE_KEY)

    response = requests.request("GET", url)
    try:
        return response.json()["Data"]["SID"]
    except KeyError:
        import time
        time.sleep(5)
        get_bearer()

def get_scooters():
    scooters = []
    url = "https://api.goflash.com/api/Mobile/Scooters"
    userLatitude = 38.70
    userLongitude = -9.16
    BEARER = get_bearer()

    for point in generate_gridpoints():
        latitude = point["lat"]
        longitude = point["lng"]
        latitudeDelta = 0.05
        longitudeDelta = 0.05


        querystring = {"userLatitude": str(userLatitude),
                    "userLongitude":str(userLongitude),
                    "lang":"en",
                    "latitude": str(latitude),
                    "longitude": str(longitude),
                    "latitudeDelta": str(latitudeDelta),
                    "longitudeDelta": str(longitudeDelta)}

        payload = ""

        headers = {
            'Authorization': "Bearer {}".format(BEARER),
            'cache-control': "no-cache",
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        scooters.extend(response.json()["Data"]["Scooters"])
    save_update_scooters(scooters)

def save_update_scooters(scooters):
    set_scooters = []
    for scooter in scooters:
        if not scooter["idScooter"] in [d['idScooter'] for d in set_scooters]:
            set_scooters.append(scooter)

    for scooter in set_scooters:
        try:
            scooter_instance = Scooter.objects.get(scooter_id=scooter["idScooter"])
            scooter_activity = ScooterActivity.objects.create(
                scooter=scooter_instance,
                lat=scooter["location"]["latitude"],
                lng=scooter["location"]["longitude"],
            )
            print("Saved new activity for existing scooter")
            scooter_activity.update_distance_travelled()
        except ObjectDoesNotExist:
            scooter_instance = Scooter.objects.create(
                scooter_id=scooter["idScooter"],
                last_lat=scooter["location"]["latitude"],
                last_lng=scooter["location"]["longitude"],
            )
            print("Saved new Scooter")
            scooter_activity = ScooterActivity.objects.create(
                scooter=scooter_instance,
                lat=scooter["location"]["latitude"],
                lng=scooter["location"]["longitude"],
            )
            print("Saved new activity for new scooter")

  