from helpers import address_helper as ah
import streamlit as st

if 'address_json' not in st.session_state:
    st.session_state.address_json = ''


def validate_button_clicked():
    given_address = st.session_state.address
    st.session_state.address_json = ah.GetLocationInfo(given_address)


st.title("Address Validator")

c1, c2 = st.columns(2)

with c1:
    st.text_area("Address", key="address")

    st.button("Validate", on_click=validate_button_clicked)
with c2:
    st.write(st.session_state.address_json)
