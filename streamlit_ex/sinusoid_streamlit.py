import streamlit as st
import numpy as np

freq = st.slider('Select frequency', 0.0, 50.0, 25.0)

t = np.linspace(0.1, 1.0, num = 10000)


x = (2*np.pi*freq*t)   # start,stop,step
y = np.sin(x)
