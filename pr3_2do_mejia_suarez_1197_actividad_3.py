print("Mejia Suarez Emmanuel Alexander_3w_1197")
# Diccionario que almacena el precio por kilo de cada fruta en pesos mexicanos
precios_frutas = {
    'manzana': 45.0,   # Precio por kilo en pesos mexicanos
    'plátano': 20.0,
    'naranja': 35.0,
    'pera': 28.0,
    'uva': 60.0
}

# Solicitar al usuario que ingrese el nombre de la fruta
fruta = input("Introduce la fruta (manzana, plátano, naranja, pera, uva): ").lower()

# Solicitar al usuario que ingrese el número de kilos de la fruta
kilos = float(input("Introduce el número de kilos: "))

# Verificar si la fruta está en el diccionario de precios
if fruta in precios_frutas:
    # Si la fruta está en el diccionario, calcular el precio total en pesos mexicanos
    precio_total = precios_frutas[fruta] * kilos
    # Mostrar el precio total formateado a dos decimales en pesos mexicanos
    print(f"El precio de {kilos} kilos de {fruta} es {precio_total:.2f} MXN")
else:
    # Si la fruta no está en el diccionario, mostrar un mensaje de error
    print("La fruta no está en el diccionario.")
