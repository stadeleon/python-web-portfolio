#  https://pypi.org/project/st-pages/
from pathlib import Path
import streamlit as st
from st_pages import Page, show_pages, add_page_title
import pandas

st.set_page_config(layout="wide")
add_page_title()
show_pages(
    [
        Page("main.py", "Home"),
        Page("pages/contacts.py", "Contact Us"),
        Page("tasks/company/main.py", "Companies"),
        Page("tasks/company/pages/contacts.py", "Company Contacts")
    ]
)

title_column_left, title_column_right = st.columns(2)

with title_column_left:
    st.image("images/photo.jpg")

with title_column_right:
    st.title("Leonid Derevianko")
    title_image_message = """
    Hi, I'm Leo a Python Software engineer, learned it with Adrit's help,
I believe my Python knowledges over background of 10 years PHP experience
will be strong enough to call myself as a good programmer %), but it's up to you 
    """
    st.info(title_image_message)

invitation_message = "Below you can find some of the apps I have built in Python. Feel free to contact me!"
st.write(invitation_message)

body_column_left, empty_column, body_column_right = st.columns([1.5, 0.5, 1.5])

data_file = pandas.read_csv("data.csv", sep=';')
separator = len(data_file) // 2
images_source = 'images/'
with body_column_left:
    for index, row in data_file[:separator].iterrows():
        st.header(row["title"])
        st.image(str(Path(images_source, row["image"])))
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with body_column_right:
    for index, row in data_file[separator:].iterrows():
        st.header(row["title"])
        st.image(str(Path(images_source, row["image"])))
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")
