import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data_exploration.csv")
st.write("Here's our first attempt at using data to create a table:")
st.write(data)

# Columns to plot
columns_to_plot = ['indor1', 'indor2', 'indor3', 'external', 'flat', 'building', 'surface']

# Display each column as a separate plot
st.write("Displaying each column as a separate plot:")

for column in columns_to_plot:
    plt.figure(figsize=(10, 6))
    plt.plot(data[column])
    plt.xlabel('Index')
    plt.ylabel(f'{column} Values')
    plt.title(f'{column} Column Visualization')
    st.pyplot(plt)
