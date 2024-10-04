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
st.markdown("**Dataset:** Laptop Price Dataset by Iron Wolf (Kaggle)")
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



# Analyzing the Average Costs of Laptop Prices by Company: Boston
st.markdown("### **`Analyzing the Average Costs of Laptop Prices by Company: Boston`**")

# Let us visualize the average costs of laptop prices (Euro) by company

# For each 'Company' the average of the 'Price (Euro)' column is calculated
avg_price_by_company = df.groupby('Company')['Price (Euro)'].mean().reset_index() # 'reset_index()' reverts it into a standard DataFrame
st.write("##### Let us visualize the average costs of laptop prices (Euro) by company")
avg_price_by_company['Price (Euro)'] = avg_price_by_company['Price (Euro)'].round(2) # Setting the significant figure to 2 decimal places
st.dataframe(avg_price_by_company)

# After visualizing the average costs of laptop prices (Euro) by company,

# We can arrange the DataFrame by the average price in descending order
avg_price_by_company = avg_price_by_company.sort_values(by='Price (Euro)', ascending=False)
st.write("##### We can arrange the DataFrame by the average price in descending order")
st.dataframe(avg_price_by_company)
st.write("We can observe here which company manufactures cheap and expensive laptops based on the average prices.")

# Now we can use a bar chart to visualize the grouped and ordered DataFrame (the average costs of laptop prices (Euro) by company)

def avg_price_by_company(): # not necessary but good practice for reusablility

    avg_price_by_company = df.groupby('Company')['Price (Euro)'].mean().reset_index()
    avg_price_by_company = avg_price_by_company.sort_values(by='Price (Euro)', ascending=False)

    # Let us create a bar chart
    plt.figure(figsize=(12, 6)) # define the width and height of the chart in inches
    plt.bar(avg_price_by_company['Company'], avg_price_by_company['Price (Euro)'], color='#009BAA')

    # Labels
    plt.title('Average Laptop Price by Manufacturer')
    plt.xlabel('Company')
    plt.ylabel('Price (Euro)')
    plt.xticks(rotation=45) # Rotate x labels for better visibility
    plt.grid(axis='y', color='#E55640') # Show horizontal grid lines to easily read corresponding prices

    st.pyplot(plt)
    plt.clf()

avg_price_by_company() # call the function

st.write("""

Based from the bar chart, we can observe that the average laptop prices differ from various companies of the dataset. 
Notably, ***Razer*** has an average price of **3346.142857**. It also records a maximum price of **6099.00** 💸 
(*see Numerical Data Description*). On the contrary, ***Vero*** which is at the bottom of the list has an average price of only **217.425000** 👌. 
The mean or average price is **1134.969059** and based from this figure we could identify which companies tend to manufacture premium and affordable laptops 💻.

""")



# Distribution of Laptop GPU Manufacturers: Boston
st.markdown("### **`Analyzing the Average Costs of Laptop Prices by Company: Boston`**")

# Let us visualize again the frequency of each GPU manufacturer or company that constitutes our dataset.
st.write("##### Let us visualize again the frequency of each GPU manufacturer or company that constitutes our dataset.")
st.write(df['GPU_Company'].value_counts())

# A pie chart will show the distribution or proportion of each GPU manufacturer/company from the dataset

def gpu_count(): # not necessary but good practice for reusablility

    gpu_count = df['GPU_Company'].value_counts()

    # Let us create a bar chart and its corresponding labels

    plt.figure(figsize = (6, 6)) # define the width and height of the chart
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] # define colors using hex value

    # Labels should correspond to its right proportion of the pie chart
    plt.pie(gpu_count, labels = ['Intel', 'Nvidia', 'AMD', 'ARM'], autopct ='%1.1f%%', startangle = 90, colors=colors)
    plt.title('Proportion of Laptop GPU Manufacturers')

    st.pyplot(plt)
    plt.clf()

gpu_count() # call the function

st.write("""

Based from the pie chart, we can observe that ***Intel*** constitutes **55.2%** 📈 or half the proportion of GPU manufacturers from the dataset. 
***Nvidia*** has a **31.1%** share which is also a popular choice. A small but notable portion comes from ***AMD*** with a share of **13.6%**. 
Lastly, **ARM**, which is considerably rare, constitutes only **0.1%** 📉 of the total distribution of GPU 💽 manufacturers from the dataset.

""")

# Distribution of Laptop Prices by Using Histogram: Zamora 
st.markdown("### **`Distribution of Laptop Prices by Using Histogram: Zamora`**")

plt.hist(df['Price (Euro)'], bins=10, color='green', alpha=0.7, edgecolor = 'black')
plt.title('Distribution of Laptop Prices')
plt.xlabel('Price (Euro)')
plt.ylabel('Number of Laptops')
st.pyplot(plt)
plt.clf()

st.write("""

The histograms display the quantity of available laptops in a specific price level. Most of the laptops that are currently manufactured in 
various regions globally can be classified as cost ranging betweeen 500 Euros and 1500 Euros. The laptops in the 1500 to 2500 euros price 
range are even fewer and there are very few laptops that cost more than 2500 euros. This implies that, though there are many quantities of 
interest in cheaper laptops, there are fewer quantities of interest in costly laptops.

""")

# Conclusion section
st.markdown("## **`Conclusion`**")
st.markdown("### **Insights from our Data Visualization and Data Analysis: 📊**")

# 1. Average Costs of Laptop Prices by Company
st.markdown("#### 1. **Average Costs of Laptop Prices by Company** 💲")
st.write("""
    - Price variation across manufacturers indicate that some companies like **_Razer, LG, and MSI_** are inclined to market on premium laptops with high-end specifications, 
    while companies such as **_Vero, Mediacom, and Chuwi_** with considerably low average prices are budget-friendly (lower performance and build quality).
    - Companies from **_Huawei_** to **_HP_** relative to the chart have a broader market, offering both premium and budget-friendly laptops.
""")

# 2. Distribution of Laptop GPU Manufacturers
st.markdown("#### 2. **Distribution of Laptop GPU Manufacturers** 💽")
st.write("""
    - The laptops from the dataset are mostly integrated with **_Intel_**'s GPU, constituting more than half (**55.2%**) of the distribution.
    - **_Nvidia_**'s GPU is also integrated into a significant portion (**31.1%**) of laptops from the dataset.
    - **_AMD_** is the third popular choice of GPU manufacturer (**13.6%**) integrated into laptops from the dataset.
    - **_ARM_** has a notably small share (**0.1%**), indicating that this GPU manufacturer is not a preferred option among the laptops.
""")