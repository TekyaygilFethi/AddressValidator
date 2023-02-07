import os
import requests
import json
from dotenv import load_dotenv
import html
from helpers import string_helper as sh

load_dotenv()
def GetLocationInfo(address):
    base_url = os.getenv('YANDEX_MAPS_BASE_URL')
    address = address.replace(" ","+")
    address = sh.convert_english(address)
    endpoint = f"{base_url}?format=json&apikey={os.getenv('YANDEX_MAPS_API_KEY')}&geocode={address}&lang=tr-TR"
    print(endpoint)

    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return "Adres Bilgisi bulunamadı!"

    return r.json()["response"]["GeoObjectCollection"]["featureMember"]