import streamlit as st
import streamlit.components.v1 as components

book_no = [i for i in range(1,13)]
book_name = ["HELLO", "WAKE UP", "SCRUB, SCRUB, SCRUB", "HIDE AND SEEK",
            "PAT, PAT, PAT","READY GO!", "THE BIRTHDAY PARTY", "YUM-YUM",
            "GO WAWY, SHADOW", "FOLLOW ME", "THE RAINY DAY", "WHO ARE YOU?" ]
base_url = f"http://media.tuntun.com/fs_qr/GSH/Book"


st.header("Guri Play")

no = st.selectbox("choice", book_no)


if no < 10:
    no = "0" + str(no)
else:
    no = str(no)

components.iframe(base_url + no, height = 800,scrolling = True)