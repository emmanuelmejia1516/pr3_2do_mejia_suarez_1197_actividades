print("Mejia Suarez Emmanuel Alexander_3w_1197")
# Solicitar al usuario que ingrese su nombre
nombre = input("Introduce tu nombre: ")

# Solicitar al usuario que ingrese su edad
edad = input("Introduce tu edad: ")

# Solicitar al usuario que ingrese su dirección
direccion = input("Introduce tu dirección: ")

# Solicitar al usuario que ingrese su número de teléfono
telefono = input("Introduce tu número de teléfono: ")

# Crear un diccionario con la información proporcionada por el usuario
persona = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Mostrar un mensaje con la información de la persona en un formato legible
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su número de teléfono es {persona['telefono']}")
