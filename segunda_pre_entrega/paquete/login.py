# función para almacenar la información
def save_data(database):
    usuario =  input("Ingrese un nombre de usuario: ")
    if usuario == usuario in database:
        print("Ya existe un usuario con este nombre. Por favor intente nuevamente.\n")
    else:
        contrasenia = input("Ingrese una contraseña: ")
        if len(contrasenia) < 7 or len(contrasenia) > 10:
            print("La contraseña debe tener entre 7 y 10 caracteres.\n")
        else:
            database[usuario] = contrasenia
            print(f"El usuario {usuario} fue registrado exitosamente.\n")

#  función para mostrar la información.
def show_data(database):
    if database.items():
        print(f"Los usuarios registrados en la base de datos son: {database}\n")
    else:
        print("La base de datos está vacía.\n")

# función para el login de usuarios
def login(database):
    intentos = 3
    if database.items():
        usuario = input("Ingresar nombre de usuario: ")
        if usuario in database:
            while intentos != 0:
                contrasenia = input("Ingrese su contraseña: ")
                if database[usuario] == contrasenia:
                    print("Sesión iniciada correctamente!\n")
                    break
                else:
                    print("La contraseña ingresada es inválida.\n")
                    intentos -= 1
                    if intentos > 0:
                        print(f"{intentos} intentos restantes.")
                    else:
                        print("No hay más intentos disponibles. Por favor intente nuevamente más tarde. \n")
                        break
    else:
        print("La base de datos está vacía.\n")

# función principal
def main():
    database = {}
    try:
        while True:
            options = input("Bienvenido/a! Por favor ingrese una opción: \n1. Crear nuevo usuario. \n2. Mostrar usuarios existentes \n3. Iniciar sesión \n0. Salir \n")
            if options == "1":
                print("Elegiste crear un nuevo usuario.")
                save_data(database)
            elif options == "2":
                show_data(database)
            elif options == "3":
                login(database)
            elif options == "0":
                print("La aplicación se cerró.")
                break
            elif options != "0" and options != "1" and options != "2" and options != "3":
                print("Por favor ingrese números del 0 al 3.\n")
    except Exception as e:
        print("Ocurrió un error inesperado en la aplicación.", e)

main()