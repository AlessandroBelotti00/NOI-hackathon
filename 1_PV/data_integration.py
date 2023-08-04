import pandas as pd
import json

file_path = "data/weather_data.json"

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

for el in data:
    print(el)