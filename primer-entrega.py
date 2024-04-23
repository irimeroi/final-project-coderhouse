# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
# Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

# Utilizar una función para almacenar la información
def save_data(database):
    usuario =  input("Ingresar nombre de usuario: ")
    if usuario == usuario in database:
        print("Ya existe un usuario con este nombre.\n")
    else:
        contrasenia = input("Ingresar contraseña: ")
        if len(contrasenia) < 7 or len(contrasenia) > 10:
            print("La contraseña debe tener entre 7 y 10 caracteres.\n")
        else:
            database[usuario] = contrasenia
            print(f"Creaste un nuevo usuario: {usuario}\n")

#  función para mostrar la información.
def show_data(database):
    if database.items():
        print(f"Los usuarios registrados en la base de datos son: {database}")
    else:
        print("La base de datos está vacía.\n")

# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
# def login(database):
    # for usuario in database:
    #     usuario = input("Ingresar nombre de usuario: ")
        # contraseña = input("Ingrese su contraseña: ")

def main():
    database = {}
    while True:
        options = int(input("Bienvenido/a! Por favor ingresar una opción: \n1. Crear nuevo usuario. \n2. Mostrar usuarios existentes \n3. Iniciar sesión \n0. Salir \n"))
        if options == 1:
            print("Elegiste crear un nuevo usuario.")
            save_data(database)
        elif options == 2:
            show_data(database)
        elif options == 3:
            # login(database)
            pass
        elif options == 0:
            print("La aplicación se cerró.")
            break
        elif options > 3:
            print("Por favor ingrese números del 0 al 3.\n")
        else:
            print("Sólo se aceptan números.\n")
main()