from helpers import address_helper as ah
import streamlit as st

if 'address_json' not in st.session_state:
    st.session_state.address_json = ''

if 'provider' not in st.session_state:
    st.session_state.provider = 'Google'


def validate_button_clicked():
    given_address = st.session_state.address
    st.session_state.address_json = ah.GetLocationInfo(given_address, st.session_state.provider)




st.title("Address Validator")


st.text_area("Address", key="address")
st.selectbox("Provider:", options=["Google","Yandex"], key="provider")
st.button("Validate", on_click=validate_button_clicked)

st.write(st.session_state.address_json)
