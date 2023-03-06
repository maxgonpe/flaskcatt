from flask import Flask, render_template
from jinja2 import FileSystemLoader
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates', static_folder='static')
app.jinja_loader = FileSystemLoader(app.template_folder)
client = MongoClient('loclahost',27017)
# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client.mantenimiento
programa = db.programa


@app.route('/')
def index():
    

    # Consulta a la colección
    mantenimientos = programa.find()

    # Renderización de la plantilla HTML con los resultados de la consulta
    return render_template('index.html', mantenimientos=mantenimientos)


# definir una ruta para modificar la colección
@app.route('/modificar_coleccion')
def modificar_coleccion():
    # obtener la colección
    coleccion = db['programa']
    documento = {}

    # modificar la estructura de un documento de la colección
    documento = coleccion.find_one({'_id': "64051fe1b3850e03db27f748"})
        
    # retornar una respuesta
    return '{ }'


if __name__ == '__main__':
    app.run()