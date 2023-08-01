import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("temperatures.txt")

st.title("Date vs Temperature Plot")

plot = px.line(x=df["date"], y=df["temperature"],
               labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(plot)
