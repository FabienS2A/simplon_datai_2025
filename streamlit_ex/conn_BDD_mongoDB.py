import streamlit as st
from pymongo import MongoClient
import pandas as pd

st.title('My first mongoDB')

client = MongoClient("localhost", 27017)

db_name = "test_db"
db = client[db_name]
#print(db)
#print(type(db))

coll = db["exo"]

infoclient = {}

email = st.text_input('label', placeholder = 'email adress', label_visibility="hidden")
if email :
    infoclient["email"] = email
name = st.text_input('label', placeholder = 'name', label_visibility="hidden")
if name :
    infoclient["name"] = name

st.write(infoclient)


if st.button('Click me'):
    st.write('You are in')
    st.success('This is a success message!', icon="✅")
    coll.insert_one(infoclient)
    cur = coll.find({})
    for doc in cur :
        st.dataframe(doc)







#print(infoclient)
client.close()