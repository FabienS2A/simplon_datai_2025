import streamlit as st
import sqlite3
import pandas as pd

st.title('My first SQLite')

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

x=()
y=()

email = st.text_input('label', placeholder = 'email adress', label_visibility="hidden")
if email :
    y = email
name = st.text_input('label', placeholder = 'name', label_visibility="hidden")
if name :
    x = name

request = [1, x, y]

if st.button('Click me'):
    st.write('You are in')
    st.success('This is a success message!', icon="✅")

    cur.execute("INSERT INTO ma_base VALUES(?, ?, ?)", request)

con.commit()



if st.button('Show Table'):
    res = cur.execute("SELECT * FROM ma_base")
    st.write(res.fetchall())
    df = pd.read_sql_table('ma_base', con)
    st.dataframe(df)




con.close()