'''import csv
import json

# Lee el archivo CSV
with open('gantt.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

# Convierte los datos a JSON
json_data = json.dumps(rows)

# Imprime el resultado
print(json_data)'''

import pandas as pd
csv_data = pd.read_csv("gantt.csv",encoding='ISO-8859-1', sep = ";")
csv_data.to_json("gantt.json", orient = "records")
