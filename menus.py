from clases import *
from guardarEnMongo import *
from guardarEnMongo import guardarEnColeccion
def menuPrincipal():
    print("------------------------------------------------------")
    print("                 MENU PRINCIPAL")
    print("------------------------------------------------------")
    print("1. Registrar")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion=int(input("Ingrese una opción: "))
    if (opcion==1):
        print("------------------------------------------------------")
        print("                    REGISTRO")
        print("           [Llene correctamente los campos]") 
        print("------------------------------------------------------")
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        email=input("Email: ")
        cedula=input("Cedula: ")
        usuarioNuevo=Usuarios(usuario,contraseña, nombre, apellido, email, cedula)
        documentoRegistro={"usuario":usuarioNuevo.usuario, "contraseña":usuarioNuevo.contraseña, "nombre":usuarioNuevo.nombre, "apellido":usuarioNuevo.apellido, "email":usuarioNuevo.email, "cedula":usuarioNuevo.cedula}
        guardarEnColeccion(documentoRegistro)
        print("------------------------------------------------------")
    elif (opcion==2):
        Usuarios.inicioSesion()