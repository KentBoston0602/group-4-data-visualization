# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from io import StringIO

st.title("Group 4_CSS145_BM7")
st.subheader("Dataset: Laptop Price Dataset")

members = [
    "Kent Patrick **BOSTON**",
    "Luis Frederick **CONDA**",
    "Chaze Kyle **FIDELINO**",
    "Joseph Isaac **ZAMORA**"
]

st.write("Members:")
for member in members:
    st.markdown(f"* {member}")

st.markdown("## **`Dataset Description`**")
st.markdown("**Dataset:** Titanic Dataset (Kaggle)")
st.markdown("https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset/code")


# Read a comma-separated values (csv) file into DataFrame
df = pd.read_csv("datasets/laptop_price - dataset.csv")
st.write(df)

buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()

st.write("Display information about our DataFrame including the index dtype and columns, non-null values and memory usage")
st.text(df_info_as_string)