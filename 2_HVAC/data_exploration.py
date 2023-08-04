import pandas as pd
import json

energy_temp = pd.read_csv("data/DatiEnergyTemp.csv", delimiter=';')
# json_file_path = "data/1_dataset.json"

# with open(json_file_path, 'r') as json_file:
#     data_dict = json.load(json_file)

# columns = list(data_dict[0])[0].split(';')

# energy_temp = pd.DataFrame(columns)

# for el in data_dict:
#     keys = list(el)[0]
#     values = el[keys].split(';')
#     keys = keys.split(';')
#     result_dict = dict(zip(keys, values))

#     energy_temp = energy_temp.append(result_dict, ignore_index=True)

# print(energy_temp)
# energy_temp.to_csv('energy_temp_cleaned.csv', index=False)