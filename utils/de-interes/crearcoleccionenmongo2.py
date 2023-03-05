import json
import pymongo

# Leer el archivo JSON
with open('project2.json') as f:
    json_data = f.read()

# Convertir el JSON a una lista de diccionarios de Python
docs = json.loads(json_data)

# Verificar que docs sea una lista no vacía
if docs:
    # Conectar a la base de datos y la colección
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['prueba']
    collection = db['peliculas']

    # Insertar los documentos en la colección
    result = collection.insert_many(docs)

    print(f"Se insertaron {len(result.inserted_ids)} documentos en la colección.")
else:
    print("La lista de documentos está vacía.")
