import os
import requests
import json
from dotenv import load_dotenv
from helpers import google_maps_service as gms, yandex_maps_service as yms

load_dotenv()


def GetLocationInfo(address, map):
    if map == "Google":
        return gms.GetLocationInfo(address)
    else:
        return yms.GetLocationInfo(address)


