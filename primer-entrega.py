# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
# Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

# Utilizar una función para almacenar la información
# def saveData():

# # función para mostrar la información.
# def showData():
#     print()
#     print()

# # Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
# def login():
#     for user in users:
#         usuario = input("Ingrese su nombre de usuario: ")
#         # contraseña = input("Ingrese su contraseña: ")

#         if usuario == user["usuario"][0]:
#             print("Correcto")
#         else:
#             print("Usuario o contraseña incorrectos.")
#     print(user)

def main():
    database = {}
    while True:
        options = int(input("Bienvenido/a! Por favor ingrese una opción: \n1. Crear nuevo usuario. \n2. Mostrar usuarios existentes \n3. Iniciar sesión \n0. Salir \n"))
        if options == 1:
            # save_data()
            nombre_de_usuario =  input("Ingrese su nombre de usuario: ")
            contrasenia = input("Ingrese su contraseña: ")
            usuario = {"usuario": nombre_de_usuario, "contrasenia": contrasenia}
            pass
        elif options == 2:
            # show_data()
            pass
        elif options == 3:
            # login()
            pass
        elif options == 0:
            print("Terminando el proceso")
            break
        elif options > 3:
            print("Por favor ingrese números del 0 al 3.")
            break
        else:
            print("Sólo se aceptan números.")
            pass
main()