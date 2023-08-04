import pandas as pd
import json

# energy_temp = pd.read_csv("data/DatiEnergyTemp.csv", encoding='latin-1', error_bad_lines=False)
# print(energy_temp.shape)  

energy_temp = pd.read_json(json_file_path)