import streamlit as st
import sqlite3
import plotly.express as px

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperatures")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

st.title("Date vs Temperature Plot")

plot = px.line(x=date, y=temperature,
               labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(plot)
