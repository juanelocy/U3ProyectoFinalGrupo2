import pymongo
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
MONGO_NOMBREDB = "sistemaDeEmergencia911"
MONGO_NOMBRECOLECCION = "usuariosRegistrados"
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_NOMBREDB]
coleccion = baseDatos[MONGO_NOMBRECOLECCION]

#-----------------------------------------------------------------------------

def guardarEnColeccion(documento):
    coleccion.insert_one(documento)


def retornarUsuarios():
    datosDeLaColeccion = coleccion.find()
    usuariosUsuarios = []
    for i in datosDeLaColeccion:
        usuariosUsuarios.append(i['usuario'])
    return usuariosUsuarios

    
def retornarContraseñas():
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['contraseña'])
    return usuariosContraseñas