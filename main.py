import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Leonid Derevianko")
    content = """
    Hi! I'm Leonid Derevianko i'm a Software engineer, learning Python programming
    language, switched from PHP with almost 10 year development experience
    """
    st.info(content)
