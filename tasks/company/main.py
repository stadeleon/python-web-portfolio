import streamlit as st
import pandas
from pathlib import Path

IMAGES_LOCATION = 'images'
DATA_FRAME_FILE = 'data.csv'


def display_column_from_data(data, start_index, stop_index):
    for index, row in data[start_index:stop_index].iterrows():
        st.subheader(f"{row['first_name']} {row['last_name']}".title())
        st.write(row['role'].title())
        st.image(str(Path(IMAGES_LOCATION, row['image'])))


st.set_page_config(layout='wide')

st.title("The Best Company")
title_message = "This is awesome description of the best company in the world"
st.write(title_message)
st.header("Our Team")

df = pandas.read_csv(DATA_FRAME_FILE)

col1, col2, col3 = st.columns(3)
with col1:
    display_column_from_data(df, None, 4)

with col2:
    display_column_from_data(df, 4, 8)

with col3:
    display_column_from_data(df, 8, None)