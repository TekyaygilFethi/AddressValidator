import os
import requests
import json
from dotenv import load_dotenv
from helpers import google_maps_service as gms, yandex_maps_service as yms

load_dotenv()


def GetLocationInfo(address, map):
    if map == "Google":
        r = gms.GetLocationInfo(address)
        results = r['results'][0]
        lat = results['geometry']['location']['lat']
        long = results['geometry']['location']['lng']

        return lat, long, r
    else:
        r = yms.GetLocationInfo(address)

        try:
            long, lat = r[0]["GeoObject"]["Point"]["pos"].split(" ")
            print(lat,long)
            return lat, long, r

        except Exception as e:
            print(e)

        return None, None, yms.GetLocationInfo(address)
