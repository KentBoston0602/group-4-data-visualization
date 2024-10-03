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

# Prints information about our DataFrame including the index dtype and columns, non-null values and memory usage.
buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()

st.write("**Display information about our DataFrame including the index dtype and columns, non-null values and memory usage**")
st.text(df_info_as_string)

# Detect missing values or sum of null values per column
st.write("**Show missing values or sum of null values per column**")
st.write(df.isna().sum())

# Numerical Data Description
st.markdown("## **`Numerical Data Description`**")
st.write(df.describe())

# Categorical Data Description
st.markdown("## **`Categorical Data Description`**")

# Categorical Data: Company
st.write("**Laptop manufacturer count sorted in descending order**")
st.write(df['Company'].value_counts())

# Categorical Data: Product
st.write("**Brand and Model count sorted in descending order**")
st.write(df['Product'].value_counts())

# Categorical Data: TypeName
st.write("**Laptop Type count sorted in descending order**")
st.write(df['TypeName'].value_counts())

# Categorical Data: CPU_Company
st.write("**Central Processing Unit manufacturer count sorted in descending order**")
st.write(df['CPU_Company'].value_counts())

# Categorical Data: CPU_Type
st.write("**Central Processing Unit type count sorted in descending order**")
st.write(df['CPU_Type'].value_counts())

# Categorical Data: Memory
st.write("**Hard Disk / SSD Memory count sorted in descending order**")
st.write(df['Memory'].value_counts())

# Categorical Data: GPU_Company
st.write("**Graphics Processing Unit manufacturer count sorted in descending order**")
st.write(df['GPU_Company'].value_counts())

# Categorical Data: GPU_Type
st.write("**Graphics Processing Unit type count sorted in descending order**")
st.write(df['GPU_Type'].value_counts())

# Categorical Data: OpSys
st.write("**Operating System count sorted in descending order**")
st.write(df['OpSys'].value_counts())