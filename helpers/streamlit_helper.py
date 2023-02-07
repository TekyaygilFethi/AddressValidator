import datetime
import streamlit as st
from helpers import folium_helper as fh, address_helper as ah
import numpy as np
from datetime import datetime, timedelta

def SetInitialStreamlitStates():
    if 'provider' not in st.session_state:
        st.session_state.provider = 'Google'

    if 'address_json_google' not in st.session_state:
        st.session_state.address_json_google = ''

    if 'address_json_yandex' not in st.session_state:
        st.session_state.address_json_yandex = ''

    if 'google_map' not in st.session_state:
        st.session_state.google_map = fh.CreateMap()

    if 'yandex_map' not in st.session_state:
        st.session_state.yandex_map = fh.CreateMap()

    if 'yandex_map_lat_long' not in st.session_state:
        st.session_state.yandex_map_lat_long = f"Koordinatlar: {[]}"

    if 'google_map_lat_long' not in st.session_state:
        st.session_state.google_map_lat_long = f"Koordinatlar: {[]}"
