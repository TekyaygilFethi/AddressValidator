import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def GetLocationInfo(address):
    base_url = os.getenv('GOOGLE_MAPS_BASE_URL')
    endpoint = f"{base_url}?address={address}&key={os.getenv('GOOGLE_MAPS_API_KEY')}"
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return "Adres Bilgisi bulunamadı!"

    return r.json()
