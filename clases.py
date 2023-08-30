from guardarEnMongo import * 
from demostrativoPyQt5 import *
class Usuarios():
    usuarios=retornarUsuarios()
    contraseñas=retornarContraseñas()
    def __init__(self, usuario, contraseña,nombre ,apellido, email, cedula ):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cedula=cedula
