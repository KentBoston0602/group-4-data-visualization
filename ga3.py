# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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