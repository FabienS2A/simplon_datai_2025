import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


st.title('Welcome to my Board')

#st.write('Are you ready for a tremendous RPG in the Universe of Simplon SUD ?')

# Personnaliser un widget bouton
#button = st.button("Click me")

if st.button('Click me'):
    st.write('You clicked on a button, well done')

age = st.slider('How old are you?', 0, 100, 25)
st.write("Vous avez ", age, 'ans')

text_input = st.text_input('label', placeholder = 'Quel est votre nom :', label_visibility="hidden")
if text_input :
    st.write("Bonjour, ", text_input, ', ça gaz ?')

agree = st.checkbox('Do you want see more ?')

if agree:
    st.write('Not today')

