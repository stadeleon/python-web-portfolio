import streamlit as st
from mailSender import send_message

st.header('Contact Us')
with st.form(key='personal_email'):
    user_email = f"Portfolio sender <{st.text_input('Email')}>"
    message_body = st.text_area("Message")
    button = st.form_submit_button("Send it to me")
    my_email = 'My Private name <any.email@any.com>'

    if button:
        send_message(user_email, my_email, message_body)
        st.info("Email successfully sent")
