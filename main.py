from helpers import address_helper as ah
import streamlit as st

"""
if 'address_json' not in st.session_state:
    st.session_state.address_json = ''
"""

if 'provider' not in st.session_state:
    st.session_state.provider = 'Google'

if 'address_json_google' not in st.session_state:
    st.session_state.address_json_google = ''

if 'address_json_yandex' not in st.session_state:
    st.session_state.address_json_yandex = ''


def validate_button_clicked():
    given_address = st.session_state.address
    # st.session_state.address_json = ah.GetLocationInfo(given_address, st.session_state.provider)
    st.session_state.address_json_google = ah.GetLocationInfo(given_address, "Google")
    st.session_state.address_json_yandex = ah.GetLocationInfo(given_address, "Yandex")




st.title("Address Validator")


st.text_area("Address", key="address")
# st.selectbox("Provider:", options=["Google","Yandex"], key="provider")
st.button("Validate", on_click=validate_button_clicked)

c1,c2 = st.columns(2)

with c1:
    st.subheader("Google")
    st.write(st.session_state.address_json_google)
with c2:
    st.subheader("Yandex")
    st.write(st.session_state.address_json_yandex)


