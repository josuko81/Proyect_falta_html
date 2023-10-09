import pandas as pd
import json

nutrition_table = pd.read_csv("./data/parte1.csv")
data_dict = nutrition_table.to_dict(orient='records') 

nombre_archivo = 'dictionary.json'
with open(nombre_archivo, 'w') as archivo:
    json.dump(data_dict, archivo, indent=4)  