from Util.mongoUtil import collection_define
from Util.mongoUtil import mongo_insert
from Util.mongoUtil import mongo_show_all
from Util.mongoUtil import mongo_find_by_id
from Util.mongoUtil import mongo_update
from Util.mongoUtil import mongo_delete
from Modelo.Collections import Articulo
from Modelo.Collections import Imagenes_Multimedia
from Modelo.Collections import Categoria
from Modelo.Collections import Etiqueta
from Modelo.Collections import Administradores
from Modelo.Collections import Interaccion


# CRUD operations for Categoria (Category) entity

def agregarCategoria(Nombre, Descripcion):
    collection_class = Categoria(Nombre, Descripcion)
    mongo_insert(collection_define(collection_class))
    print("Categoria added:", Nombre, Descripcion)

def mostrarCategorias():
    print(mongo_show_all('Categoria'))


# CRUD operations for Articulo (Article) entity

def agregarArticulo(Titulo, Contenido, Fecha_publicacion, Autor, Categoria, Etiquetas):
    collection_class = Articulo(Titulo, Contenido, Fecha_publicacion, Autor, Categoria, Etiquetas)
    mongo_insert(collection_define(collection_class))
    print("Articulo added:", Titulo, Contenido, Fecha_publicacion, Autor, Categoria, Etiquetas)

def mostrarArticulos():
    print(mongo_show_all('Articulo'))

def mostrarArticuloPorId(id):
    article = mongo_find_by_id('Articulo', id)
    if article:
        print(article)
    else:
        print("Article with ID", id, "not found")

def actualizarArticulo(id, Titulo, Contenido, Fecha_publicacion, Autor, Categoria, Etiquetas):
    update_data = {
        "Titulo": Titulo,
        "Contenido": Contenido,
        "Fecha_publicacion": Fecha_publicacion,
        "Autor": Autor,
        "Categoria": Categoria,
        "Etiquetas": Etiquetas
    }
    mongo_update('Articulo', id, update_data)
    print("Article updated successfully")

def eliminarArticulo(id):
    mongo_delete('Articulo', id)
    print("Article deleted successfully")


def agregarImagenes_Multimedia(Nombre, Url):
    collection_class = Imagenes_Multimedia(Nombre, Url)
    mongo_insert(collection_define(collection_class))
    print("Imagenes_Multimedia added:", Nombre, Url)

def mostrarImagenes_Multimedia():
    print(mongo_show_all('Imagenes_Multimedia'))


def agregarEtiqueta(Nombre, Descripcion):
    collection_class = Etiqueta(Nombre, Descripcion)
    mongo_insert(collection_define(collection_class))
    print("Etiqueta added:", Nombre, Descripcion)

def mostrarEtiquetas():
    print(mongo_show_all('Etiqueta'))


def agregarAdministradores(Nombre_Usuario, Correo_Electronico, Contraseña):
    collection_class = Administradores(Nombre_Usuario, Correo_Electronico, Contraseña)
    mongo_insert(collection_define(collection_class))
    print("Administradores added:", Nombre_Usuario, Correo_Electronico, Contraseña)

def mostrarAdministradores():
    print(mongo_show_all('Administradores'))


def agregarInteraccion(Tipo_Interaccion, Fecha_Interaccion, Calificacion, Comentario):
    collection_class = Interaccion(Tipo_Interaccion, Fecha_Interaccion, Calificacion, Comentario)
    mongo_insert(collection_define(collection_class))
    print("Interaccion added:", Tipo_Interaccion, Fecha_Interaccion, Calificacion, Comentario)

def mostrarInteracciones():
    print(mongo_show_all('Interaccion'))


