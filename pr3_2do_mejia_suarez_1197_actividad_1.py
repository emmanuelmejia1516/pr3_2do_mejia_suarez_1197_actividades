print("Mejia Suarez Emmanuel Alexander_3w_1197")
# Diccionario que almacena las divisas y sus símbolos respectivos
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Se solicita al usuario que ingrese el nombre de una divisa
divisa_usuario = input("Introduce una divisa (Euro, Dollar, Yen): ")

# Se verifica si la divisa ingresada se encuentra en el diccionario
if divisa_usuario in divisas:
    # Si la divisa está en el diccionario, se muestra su símbolo
    print(f"El símbolo de {divisa_usuario} es {divisas[divisa_usuario]}")
else:
    # Si la divisa no está en el diccionario, se muestra un mensaje de error
    print("La divisa no está en el diccionario.")
