from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.mantenimiento


@app.route('/')
def index():
    # Conexión a la base de datos
    client = MongoClient('localhost', 27017)
    db = client.mantenimiento
    programa = db.programa

    # Consulta a la colección
    mantenimientos = programa.find()

    # Renderización de la plantilla HTML con los resultados de la consulta
    return render_template('index.html', mantenimientos=mantenimientos)


@app.route('/ver')
def ver_mantenimiento():
    # Conexión a la base de datos
    client = MongoClient('localhost', 27017)
    db = client.mantenimiento
    programa = db.programa

    # Consulta a la colección
    mantenimientos = programa.find()

    # Renderización de la plantilla HTML con los resultados de la consulta
    return render_template('ver_mantenimiento.html', mantenimientos=mantenimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def agregar_mantenimiento():
    #db = cliente['nombre_de_tu_bd']
    coleccion = db['programa']
    # si el método de la petición es POST, guardar el nuevo documento en la base de datos
    if request.method == 'POST':
        # obtener los datos del formulario
        equipo = request.form['equipo']
        area = request.form['area']
        actividades = request.form['actividades']
        frecuencia = request.form['frecuencia']
        responsable = request.form['responsable']
        meses = request.form['meses']

        # crear el documento
        documento = {
            'equipo': equipo,
            'area': area,
            'actividades': actividades,
            'frecuencia': frecuencia,
            'responsable': responsable,
            'meses': meses
        }

        # insertar el documento en la base de datos
        coleccion.insert_one(documento)

        # redirigir a la página principal
        return redirect(url_for('ver_mantenimiento'))

    # si el método de la petición es GET, mostrar el formulario para ingresar los datos
    return render_template('nuevo_mantenimiento.html')


@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar_mantenimiento(id):
    #coleccion = conexionMongo()
    coleccion = db['programa']
    mantenimiento = coleccion.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        # Obtener los datos del formulario
        equipo = request.form['equipo']
        area = request.form['area']
        actividades = request.form['actividades']
        frecuencia = request.form['frecuencia']
        responsable = request.form['responsable']
        meses = request.form.getlist('meses')

        # Actualizar los datos del mantenimiento en la base de datos
        coleccion.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'equipo': equipo,
                'area': area,
                'actividades': actividades,
                'frecuencia': frecuencia,
                'responsable': responsable,
                'meses': meses
            }}
        )

        # Redirigir de vuelta a la página de lista de mantenimientos
        return redirect(url_for('ver_mantenimiento'))

    # Renderizar la plantilla de edición con los datos actuales del mantenimiento
    return render_template('editar_mantenimiento.html', mantenimiento=mantenimiento)



@app.route('/eliminar/<id>', methods=['POST'])
def eliminar_mantenimiento(id):
    coleccion = db['programa']
    coleccion.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('ver_mantenimiento'))


if __name__ == '__main__':
    app.run()

