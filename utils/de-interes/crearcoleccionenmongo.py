import pymongo
import json

# Establecer una conexión con la base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["prueba"]

# Cargar el archivo JSON en una variable Python
with open('project2.json') as f:
    datos = json.load(f)

# Obtener la colección donde se insertarán los documentos
colección = db["peliculas"]

# Insertar los documentos en la colección
resultado = colección.insert_many(datos)

# Imprimir los ID de los documentos insertados
print(resultado.inserted_ids)
