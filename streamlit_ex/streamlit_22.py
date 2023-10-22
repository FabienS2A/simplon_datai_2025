import streamlit as st
import numpy as np

st.title("Personnalisation des widgets")

# Personnaliser un widget bouton
button = st.button("Click here and you'll get a nice Surprise !")

# Utiliser du HTML pour personnaliser le bouton
button_html = """
<style>
    .stButton>button {
        background-color: cyan;
        color: black;
        border: 1px solid black;
        border-radius: 40px;
    }
</style>
"""
st.markdown(button_html, unsafe_allow_html=True)





if button:
    st.write("Isn't it Cool !")


    

