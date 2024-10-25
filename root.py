import streamlit as st
import time
from security import check_password, check_api_key
from layout import create_header, set_background, emptylines
from form_handler import handle_form_submission

# Set up layout and background
create_header()
set_background()
emptylines()
st.markdown("---")

# Initial session state
if "password_verified" not in st.session_state:
    st.session_state.password_verified = False

if "api_key_verified" not in st.session_state:
    st.session_state.api_key_verified = False

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Helper function to trigger a safe rerun
def safe_rerun():
    # Use a flag to manage rerun state
    if "rerun_trigger" not in st.session_state:
        st.session_state.rerun_trigger = True
        st.experimental_rerun()

# Password input section
if not st.session_state.password_verified:
    st.title("Login")
    password = st.text_input("Enter password", type="password", key="password_input")

    if st.button("Submit Password"):
        if check_password(password):
            st.session_state.password_verified = True
            
            # Use a placeholder for the success message
            success_placeholder = st.empty()
            success_placeholder.success("Password verified!")
            
            # Set a rerun trigger after displaying success
            st.session_state.rerun_trigger = True
        else:
            st.error("Invalid password!")

# API key input section
if st.session_state.password_verified and not st.session_state.api_key_verified:
    st.title("API Key Verification")
    api_key = st.text_input("Enter API key", type="password", key="api_key_input")

    if st.button("Submit API Key"):
        if check_api_key(api_key):
            st.session_state.api_key_verified = True
            st.session_state.api_key = api_key
            
            # Use a placeholder for the success message
            success_placeholder = st.empty()
            success_placeholder.success("API key verified!")
            
            # Set a rerun trigger after displaying success
            st.session_state.rerun_trigger = True
        else:
            st.error("Invalid API key!")

# Trigger rerun safely if the flag is set
if st.session_state.get("rerun_trigger", False):
    time.sleep(1)  # Optional delay for user to see the success message
    st.session_state.rerun_trigger = False  # Reset the trigger
    st.experimental_rerun()

# Handle form submission when both password and API key are verified
if st.session_state.password_verified and st.session_state.api_key_verified:
    handle_form_submission()
