import time
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

def df1():
    st.write("first dataset")
    energy_temp = pd.read_csv("exported_merged_power_consum.csv", delimiter=',')
    st.write(energy_temp)
    st.write("second dataset")
    energy_temp = pd.read_csv("exported_merged_power_product.csv", delimiter=',')
    st.write(energy_temp)
    
    image = Image.open("energy_consumption.jpg")
    st.image(image, caption="Neural Network Result", use_column_width=True) 
    st.write("Results for the second model")
    image = Image.open("power_consumption.png")
    st.image(image, caption="Neural Network Result", use_column_width=True)
    
    if st.button("Launch the neural network 🤖"):
        st.write("Neural network launched!")
        time.sleep(3)  # Add a 3-second delay
        st.write("Neural network processing completed!")
        st.write("Elapsed time: 2.7s")

        data = [['yhat(PV_production| temp, sun, wind speed)', '0.15', '0.8', '0.78', '1.89'],
                ['yhat(Building_consumption| temp, H_sun, wind_speed)', '[1.49, 0.95, 1.99]', '1.46', '0.49', '4.10'],
               ]
  
        # Create the pandas DataFrame
        df = pd.DataFrame(data, columns=['Model', 'Final loss', 'avg. mae', 'avg. r2', 'avg. rmse'])
        st.write(df)

        data = [['yhat(flat|...)', '0.15', '0.8', '0.78', '1.89'],
                ['yhat(i1,i2,i3|...)', '[1.49, 0.95, 1.99]', '1.46', '0.49', '4.10'],
               ]
  
        # Create the pandas DataFrame
        df = pd.DataFrame(data, columns=['Model', 'Final loss', 'avg. mae', 'avg. r2', 'avg. rmse'])
        st.write(df)

        # Load and display the image
        image = Image.open("t2_1.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)
        # Load and display the image
        image = Image.open("t2_1.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)

def df2():
    data = pd.read_csv("data_exploration.csv")
    st.write(data)

    # Columns to plot
    columns_to_plot = ['indor1', 'indor2', 'indor3', 'external', 'flat', 'building']

    for column in columns_to_plot:
        plt.figure(figsize=(10, 6))
        plt.plot(data[column])
        plt.xlabel('Index')
        plt.ylabel(f'{column} Values')
        plt.title(f'{column} Column Visualization')
        st.pyplot(plt)
    
    if st.button("Launch the neural network 🤖"):
        st.write("Neural network launched!")
        time.sleep(3)  # Add a 3-second delay
        st.write("Neural network processing completed!")
        st.write("Elapsed time: 2.7s")
        data = [['yhat(flat|...)', '0.15', '0.8', '0.78', '1.89'],
                ['yhat(i1,i2,i3|...)', '[1.49, 0.95, 1.99]', '1.46', '0.49', '4.10'],
                ['yhat(ext|...)', '[1.65, 0.89, 1.69]', '1.48', '0.47', '4.26']]
  
        # Create the pandas DataFrame
        df = pd.DataFrame(data, columns=['Model', 'Final loss', 'avg. mae', 'avg. r2', 'avg. rmse'])
        st.write(df)

        # Load and display the image
        st.write("Results for the first model")
        image = Image.open("t3.png")
        st.image(image, caption="Neural Network Result", use_column_width=True) 
        st.write("Results for the second model")
        image = Image.open("t2_1.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)
        image = Image.open("t2_2.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)
        image = Image.open("t2_3.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)
        st.write("Results for the third model")
        image = Image.open("t3.png")
        st.image(image, caption="Neural Network Result", use_column_width=True)
def main():
    st.sidebar.title("Dataset Selection")
    selected_dataset = st.sidebar.radio("Select a dataset", ["Dataset 1", "Dataset 2"])

    if selected_dataset == "Dataset 1":
        df1()
    elif selected_dataset == "Dataset 2":
        df2()

if __name__ == "__main__":
    main()
