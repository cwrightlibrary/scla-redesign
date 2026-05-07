import streamlit as st

st.title("Admin")

st.header("Edit Home")
@st.dialog("Edit Home")
def edit_home():
    text = st.text_area("Text to add")
    if st.button("Add"):
        with open("src/pages/home.py", "a", encoding="utf-8") as f:
            f.write(f'st.write("{text}")')

if st.button("Add text to home page"):
    edit_home()