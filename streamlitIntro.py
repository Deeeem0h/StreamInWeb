import streamlit as st

name = st.text_input("Your Name", "Des")
age = st.slider("Your Age", 0, 100, 32)

st.write(f"Q hongo, {name}, Tienes {age} años")

