from helpers import address_helper as ah, folium_helper as fh, streamlit_helper as sh
from streamlit_folium import folium_static, st_folium
import streamlit as st

sh.SetInitialStreamlitStates()

def validate_button_clicked():
    given_address = st.session_state.address
    google_lat, google_long, st.session_state.address_json_google = ah.GetLocationInfo(given_address, "Google")
    yandex_lat, yandex_long, st.session_state.address_json_yandex = ah.GetLocationInfo(given_address, "Yandex")

    st.session_state.google_map = fh.CreateMap([google_lat, google_long])
    st.session_state.yandex_map = fh.CreateMap([yandex_lat, yandex_long])

    st.session_state.google_map_lat_long = f"Koordinatlar: {[google_lat, google_long]}"
    st.session_state.yandex_map_lat_long = f"Koordinatlar: {[yandex_lat, yandex_long]}"

st.title("Address Validator")

st.text_area("Address", key="address")

st.button("Validate", on_click=validate_button_clicked)

c1, c2 = st.columns(2)

with c1:
    st.subheader("Google")
    st_folium(fig=st.session_state.google_map, key="gmap", height=400)
    st.markdown(st.session_state.google_map_lat_long)
    st.write(st.session_state.address_json_google)
with c2:
    st.subheader("Yandex")
    st_folium(fig=st.session_state.yandex_map, key="ymap", height=400)
    st.markdown(st.session_state.yandex_map_lat_long)
    st.write(st.session_state.address_json_yandex)
