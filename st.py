import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Iris Dataset Analysis")
data = pd.read_csv("./data/HousePricePrediction/train.csv")
st.write(data)

