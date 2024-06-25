users = {
    "jaramillo": "1234"
}

def registrar():
    nombre_usuario = input("Ingresa un nombre de usuario: ")
    if nombre_usuario in users:
        print("El usuario ya existe. Intenta con otro nombre.")
    else:
        contraseña = input("Ingresa una contraseña: ")
        users[nombre_usuario] = contraseña
        print("Usuario registrado correctamente.")

def iniciar_sesion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    if nombre_usuario in users and users[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def mostrar():
    print("\nUsuarios registrados:")
    for usuario, contraseña in users.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        mostrar()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
