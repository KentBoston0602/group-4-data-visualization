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

# Ram vs Price of Laptops by Using Scatter Plot: Zamora 
st.markdown("### **`Ram vs Price of Laptops by Using Scatter Plot: Zamora`**")

plt.scatter(df['RAM (GB)'], df['Price (Euro)'], edgecolor='black')
plt.title('RAM vs Price of Laptops')
plt.xlabel('RAM (GB)')
plt.ylabel('Price (Euro)')
st.pyplot(plt)
plt.clf()

st.write("""

In general, the price of the laptop tends to go high when the RAM is high. This suggest that the two variables 
are positively related. This is a really interesting thing: laptops with equal amounts of RAM can cost a lot of 
money. This implies that RAM is not the only determinant of the price of a computer. It is also likely that other 
characteristics such as the processor, type of storage, graphic card, brand, and display probably contribute to it. 
There is a laptop that has 64 GB RAM which is actually cheaper than some laptops which have a much lower RAM. This 
could be an anomaly, a record that is quite different from the other records and could be followed up on.

""")

# Average CPU Frequency Analysis by Laptop Type: Fidelino 
st.markdown("### **`Average CPU Frequency Analysis by Laptop Type: Fidelino`**")

def avg_GHz_by_type(): # not necessary but good practice for reusablility

    avg_GHz_by_type = df.groupby('TypeName')['CPU_Frequency (GHz)'].mean().reset_index()
    avg_GHz_by_type = avg_GHz_by_type.sort_values(by='CPU_Frequency (GHz)', ascending=True)

    # Let us create a bar chart
    plt.figure(figsize=(12, 6)) # define the width and height of the chart in inches
    plt.bar(avg_GHz_by_type['TypeName'], avg_GHz_by_type['CPU_Frequency (GHz)'], color='#BAD8EB')

    # Labels
    plt.title('Average CPU Frequency (GHz) by Laptop Type')
    plt.xlabel('TypeName')
    plt.ylabel('CPU_Frequency (GHz)')
    plt.grid(axis='y', color='#feaab9') # Show horizontal grid lines to easily read corresponding prices

    st.pyplot(plt)
    plt.clf()

avg_GHz_by_type() # call the function

# Calculate the average CPU Frequency for each TypeName
average_cpu_frequency = df.groupby('TypeName')['CPU_Frequency (GHz)'].mean().reset_index()

# Rename the columns for clarity
average_cpu_frequency.columns = ['TypeName', 'Average_CPU_Frequency (GHz)']

# Sort the DataFrame by Average_CPU_Frequency in descending order
average_cpu_frequency = average_cpu_frequency.sort_values(by='Average_CPU_Frequency (GHz)', ascending=False).reset_index(drop=True)

# Print the result without index numbering
st.dataframe(average_cpu_frequency)
st.write("""

According to the "Average CPU Frequency Analysis by Laptop Type" chart, laptops that are designed for workstations have the highest CPU frequency with **2.75 GHz** which is essential for complex data processing, high-performance computing, software development and compilation, etc. Gaming laptops, with an average CPU frequency of **2.72 GHz** requires a high performance CPU due to the increasingly high processing demand of PC games. Ultrabook follows with an average of **2.3 GHz**, offering a blend of performance and portability that is ideal for users who need a powerful yet lightweight device. Furthermore, Notebooks has an average CPU frequency of **2.21 GHz** which is perfect for a user that prioritizes efficiency and mobility. The 2 in 1 Convertible, on the other hand, has an average of **2.12 GHz** which offers flexibility and are designed to users that wants a device that can serve as both a laptop and a tablet. Lastly, with an average CPU frequency of **1.68 GHz** the Netbook is designed for basic computing tasks and is suitable for users that prioritizes portability in devices.

""")

# Distribution of CPU Manufacturers: Fidelino 
st.markdown("### **`Distribution of CPU Manufacturers: Fidelino`**")

st.write(df['CPU_Company'].value_counts())

def cpu_count():

    cpu_count = df['CPU_Company'].value_counts()

    #bar chart and its corresponding labels

    plt.figure(figsize = (6, 6)) # define the width and height of the chart
    colors = ['#0175a4', '#01af82', '#f3bc01']

    # Labels should correspond to its right proportion of the pie chart
    plt.pie(cpu_count, labels = ['Intel', 'AMD', 'Samsung'], autopct ='%1.1f%%', startangle = 0, colors=colors, explode=(0.1, 0.1, 0.1)) # separate the slices for better visibility
    plt.title('Distribution of CPU Brands')

    st.pyplot(plt)
    plt.clf()

cpu_count() # call the function

st.write("""

The market share for various CPU brands used in laptop manufacture is shown in the pie chart "Distribution of CPU Brands". **95.2%** of laptops made have Intel CPUs, which is a huge domination in the chart. This suggests that Intel is the clear market leader for laptop CPUs. AMD CPUs, on the other hand, are found in **4.7%** of laptops, which is a considerably smaller yet noticeable presence. Lastly, compared to AMD and Intel, Samsung CPUs have a very small market share of **0.1%**, indicating their restricted usage in laptops. This distribution highlights Intel's dominant market share and the very small share of other CPU manufacturers in the laptop market, such as AMD and Samsung.

""")

# Average Costs of Laptop Prices by Screen Size: Conda
st.markdown("### **`Average Costs of Laptop Prices by Screen Size: Conda`**")

# Calculate the average price by screen size (inches)
avg_price_by_screen_size = df.groupby('Inches')['Price (Euro)'].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.scatter(avg_price_by_screen_size['Inches'], avg_price_by_screen_size['Price (Euro)'], color='red', s=100, edgecolor='black') # s=100 sets the size of the points for better visibility

# Add labels and title
plt.xlabel('Screen Size (Inches)')
plt.ylabel('Average Price (Euro)')
plt.title('Average Laptop Price by Screen Size')
plt.grid(True)

st.pyplot(plt)
plt.clf()

st.write("""

There is not a 100% direct relationship, but over arching, it can be inferred that the larger the screen size, the higher the average laptop price.

This is why variations from the typical pattern seen within the central group of data points can also appear in other factors, such as laptop brands, features, and more.

""")

# Average Laptop Price by GPU Company: Conda
st.markdown("### **`Average Laptop Price by GPU Company: Conda`**")

# Calculate the average price for each GPU Company
avg_price_by_GPUcompany = df.groupby('GPU_Company')['Price (Euro)'].mean().reset_index()

# We can arrange the DataFrame by the average price in descending order
avg_price_by_GPUcompany = avg_price_by_GPUcompany.sort_values(by='Price (Euro)', ascending=False)

# Create a bar plot for Average Cost by GPU Company
plt.figure(figsize=(12, 6))
sns.barplot(x='Price (Euro)', y='GPU_Company', data=avg_price_by_GPUcompany, palette='viridis', hue='GPU_Company', legend=False)
plt.title('Average Laptop Price by GPU_Company')
plt.xlabel('Average Price (Euro)')
plt.ylabel('GPU Company')
plt.grid(axis='x', color='#BA8E23')

st.pyplot(plt)
plt.clf()

st.write("""

As it was expected, laptops equipped with Nvidia GPUs are the most expensive; their average price is a little bit over 1500 Euros. Currently, laptops with Intel GPUs are a little over 1000 Euros, AMD GPUs are between 800 Euros, ARM GPUs are about 600 Euros.

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

# 3. Distribution of Laptop Prices
st.markdown("#### 3. **Distribution of Laptop Prices** 💻")
st.write("""
    - The histogram below shows the prices for the laptops. They indicate that the majority of laptops are in the price segment of 500 to 1500 Euros.
    - The best way to illustrate the variability in the distribution is to show that as the price increases the number of laptops sold reduces and therefore we have a positively skewed distribution. From this we can deduce that there are a few costly laptops, however, a majority of them fall under the low-end category.
""")

# 4. RAM vs Price of Laptops
st.markdown("#### 4. **RAM vs Price of Laptops** 🎫")
st.write("""
    - The paper further establishes that there is a positive correlation between RAM and price of laptops but it is not as simple.
    - Specifically other attributes like the processor, storage type, graphics card, brand and screen quality also influence the laptop prices.
    - Hence, while buying a laptop, one has to look at the whole set of parameters and characteristics to get the maximum of benefits for the given price/amount of money, not just RAM.	 
""")

# 5. Average CPU Frequency Analysis by Laptop Type
st.markdown("#### 5. **Average CPU Frequency Analysis by Laptop Type** 📡")
st.write("""
    - CPU Frequencies are often designed and calibrated based on the type and function of the laptop. The purpose of having a specific range of CPU frequencies is to support the supposed task of each laptop types with the highest possible performance and efficiency.
    - Tasks vary and therefore when efficiency and performance is being negatively affected, despite having the correct type of laptop or device, users are able to modify the device's electronic circuit's timing settings to run at a lower or higher clock rate than is specified, which is called underclocking and overclocking.
""")

# 6. Distribution of CPU Manufacturers
st.markdown("#### 6. **Distribution of CPU Manufacturers** 📟")
st.write("""
    - **Intel** accounts for majority of the CPU used by laptop manufacturers which clearly indicates their current dominance in that market.
    - 4.7 percent of laptops have **AMD** CPUs. This still constitutes a sizeable portion of the market, even though it is far smaller than Intel's share. Given Intel's dominance, AMD's presence indicates a significant with less market importance.
    - **Samsung** CPUs only account for 0.1% of the market. This poor presence indicates that Samsung is not a major participant in this area and emphasizes their low penetration into the laptop CPU market.	 
""")