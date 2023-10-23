import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import scipy.stats
from scipy.stats import norm

st.title('Reading and displaying tab files')


with st.sidebar:
    type = st.radio(
        "Select a file type",
        ("csv files", "json files", "excel files")
    )

if type == "csv files" :
    st.header("Lecture de données depuis un fichier csv")
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

if type == "json files" :
    st.header("Lecture de données depuis un fichier json")
    uploaded_files = st.file_uploader("Choose a json file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        df = pd.read_json(uploaded_file)
        st.dataframe(df)

if type == "excel files" :
    st.header("Lecture de données depuis un fichier excel")
    uploaded_files = st.file_uploader("Choose a excel file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        df = pd.read_excel(uploaded_file, orient='index')
        st.dataframe(df)