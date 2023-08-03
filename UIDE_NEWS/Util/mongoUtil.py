from Conexion.mongo import collection_config
from Modelo.Manager import Collection, Sesion

def collection_define(collection_class_selector):
    collection_class=collection_class_selector
    collection_name=collection_class.__class__.__name__
    collection_document = collection_class.get_document()
    collection_manager= Collection(collection_name,collection_document)
    return collection_manager

def mongo_find_id(nombre,buscar):
    collection=collection_config(nombre)
    result = collection.find_one({""+buscar[0]+"": ""+buscar[1]+"",})
    return str(result["_id"])
  
def mongo_find(nombre,buscar):
    collection=collection_config(nombre)
    result = collection.find_one({""+buscar[0]+"": ""+buscar[1]+"",})
    return str(result)


def mongo_show(nombre):
    collection=collection_config(nombre)
    result = collection.find_one()
    return str(result)

def mongo_show_all(nombre):
    collection=collection_config(nombre)
    result = collection.find()
    return str(result)
    

def mongo_insert(colletion_manager):
    collection=collection_config(colletion_manager.get_name())
    collection.insert_one(colletion_manager.get_document())
    
def mongo_update(nombre, id, data):
    collection = collection_config(nombre)
    result = collection.update_one({"_id": id}, {"$set": data})
    if result.modified_count > 0:
        print("Document updated successfully")
    else:
        print("Document not found or not updated")

def mongo_delete(nombre, id):
    collection = collection_config(nombre)
    result = collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        print("Document deleted successfully")
    else:
        print("Document not found or not deleted")

def mongo_find_by_id(nombre, id):
    collection = collection_config(nombre)
    result = collection.find_one({"_id": id})
    return result

def mongo_find_by_email(nombre, email):
    collection = collection_config(nombre)
    result = collection.find_one({"Correo_Electronico": email})
    return result

def autentication(nombre, email, password):
    collection = collection_config(nombre)
    user = collection.find_one({"email": email})
    if user is None:
        return False, "Usuario no encontrado"
    stored_password = user.get("Contraseña")

    if stored_password == password:
        return True, "Contraseña válida"
    else:
        return False, "Contraseña incorrecta"


def iniciar_sesion(nombre,email,password):
    validador = autentication(nombre,email,password)
    if (validador==True):
        ini = Sesion(validador)


   
