import pandas as pd

file_path = '2_HVAC\data\data.csv'
df = pd.read_csv(file_path, delimiter=';', lineterminator='\n')
print(df.head(5))