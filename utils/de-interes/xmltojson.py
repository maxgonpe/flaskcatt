import xmltodict
import json

# Lee el archivo XML
with open('project1.xml', 'r') as f:
    xml_data = f.read()

# Convierte el XML a un objeto Python
py_data = xmltodict.parse(xml_data)

# Convierte el objeto Python a JSON
json_data = json.dumps(py_data)

# Imprime el resultado
print(json_data)



with open('project1.xml') as f:
    doc = xmltodict.parse(f.read())

diccionario = doc

with open('project1.json', 'w') as f:
    json.dump(diccionario, f)


