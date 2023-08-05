import pandas as pd
import datetime
from matplotlib import pyplot as plt

building_consumption = pd.read_csv("data/Office building.csv")
building_production = pd.read_csv("data/PV plant.csv")

print(f"building_consumption COLUMNS: {building_consumption.columns}")
print(f"building_production COLUMNS: {building_production.columns}")

data_series = []

for index, row in building_consumption.iterrows():
    timestamp_string = row['Timestamp']
    # Split the string into time and timezone parts
    time_part, timezone_part = timestamp_string.split("+")

    # Split the time part into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_part.split(":"))

    dt = datetime(row['Year'], row['Month'], row['Day'], hours, minutes, seconds)
    #dt = datetime(row['Year'], row['Month'], row['Day'])

    data_series.append(dt)
building_consumption['Timestamp'] = data_series


avg_power_consum = building_consumption.groupby('Timestamp')['Energy (Wh)'].mean()
avg_power_consum = (pd.DataFrame(avg_power_consum))
plt.scatter(avg_power_consum.index, avg_power_consum['Energy (Wh)'], color='blue')
plt.title('Medium building consumption')
plt.xlabel('Timestamp')
plt.ylabel('Energy (Wh)')

data_series = []
for index, row in building_production.iterrows():
    timestamp_string = row['Timestamp']
    # Split the string into time and timezone parts
    time_part, timezone_part = timestamp_string.split("+")

    # Split the time part into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_part.split(":"))

    #dt = datetime(row['Year'], row['Month'], row['Day'], hours, minutes, seconds)
    dt = datetime(row['Year'], row['Month'], row['Day'])

    data_series.append(dt)
building_production['Timestamp'] = data_series

avg_power_product = building_production.groupby('Timestamp')['Power (W)'].mean()
avg_power_product = (pd.DataFrame(avg_power_product))
avg_power_product['Energy (Wh)'] = avg_power_product['Power (W)']/6

plt.scatter(avg_power_product.index, avg_power_product['Energy (Wh)'], color='blue')
plt.title('Medium building production')
plt.xlabel('Timestamp')
plt.ylabel('Energy (Wh)')
plt.show()