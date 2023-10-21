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

freq = st.slider('Select frequency', 0.0, 50.0, 25.0)

t = np.linspace(0.1, 1.0, num = 10000)

#for i in range(10):
  #x = np.arange(i,i+2*np.pi,0.1)   # start,stop,step
  #y = np.sin(x)
  #st.line_chart(y)


x = (2*np.pi*freq*t)   # start,stop,step
y = np.sin(x)
st.line_chart(y)