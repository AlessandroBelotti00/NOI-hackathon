import pandas as pd
import matplotlib.pyplot as plt

file_path = '2_HVAC\data\data.csv'
df = pd.read_csv(file_path, delimiter=';')
print(df.head(5))