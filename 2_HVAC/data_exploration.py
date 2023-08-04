import pandas as pd
from matplotlib import pyplot as plt

energy_temp = pd.read_csv("data/data.csv", delimiter=';')

energy_temp['external'].apply(pd.to_numeric, errors='coerce')
print(energy_temp.dtypes)

energy_temp['external'] = [float(value) for value in energy_temp['external']]


plt.scatter(energy_temp['timestamp'], energy_temp['external'], color='blue')
plt.title('Medium building consumption')
plt.xlabel('Timestamp')
plt.ylabel('Energy (Wh)')

# energy_temp.to_csv('energy_temp_cleaned.csv', index=False)