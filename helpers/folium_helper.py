import folium
from folium.plugins import HeatMap
from helpers import address_helper as ah


def CreateMap(my_latlong=None, zoom_start=15):
    if my_latlong is None or None in my_latlong:
        my_latlong = [38.7792, 35.4572]

    m = folium.Map(my_latlong, zoom_start=zoom_start)
    folium.Marker(
        my_latlong, popup="Konumum", tooltip="Konumum"
    ).add_to(m)

    return m
