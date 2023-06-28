import streamlit as st
from pandas import read_csv
from companyMailSender import send_message

st.header('Contact Us')
topics = read_csv('topics.csv')

with st.form(key='company_email'):
    name = st.text_input('Your Name')
    user_email = f"{name} <{st.text_input('Email')}>"
    subject = st.selectbox("Select the topic", topics['topic'].tolist())
    message = st.text_area("Message")
    button = st.form_submit_button("Send")
    my_email = 'My Company Site <leo@leo.com>'

    if button:
        send_message(user_email, my_email, message, subject)
        st.info("Email sent successfully")
