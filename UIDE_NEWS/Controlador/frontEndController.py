from flask import Flask, render_template, request
from Controlador.Controlador import (agregarCategoria)
import os

# Get the absolute path of the current directory (another_folder)
current_directory = os.path.abspath(os.path.dirname(__file__))
template_folder = os.path.join(current_directory, '..', 'templates')
static_folder = os.path.join(current_directory, '..', 'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categoria')
def categoria():
    return render_template('agregarCategoria.html')

@app.route('/agregarCategoria', methods=['GET', 'POST'])
def agregar_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        agregarCategoria(nombre, descripcion)
        return "Category added successfully!"
    else:
        return render_template('agregarCategoria.html')

if __name__ == '__main__':
    app.run(debug=True)