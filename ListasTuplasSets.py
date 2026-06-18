# Listas
# Guarda muchos valores en una sola variable
# Se escribe entre corchetes
# seria como una estantería con cajones numerados
# acepta repetidos


frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
# for se puede recorrer en un bucle, 
# como ir leyendo cajoncito por cajoncito
    print(fruta)
# manzana, banana, cereza

# Strings
# Recorre una cadena de texto letra por letra
palabra = "Python"
for letra in palabra:
    print(letra, end="-")
# P-y-t-h-o-n-

# Diccionarios (claves y valores)
# son cajones con nombre "vida", "nombre"
persona = {"nombre": "Ana", "edad": 25}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Sets y Tuplas
# un set es como un montón de cosas sin orden 
# y sin repetidos
# Tuplas es una lista ordenada, NO se puede cambiar
# y acepta repetidos
coordenadas = (10, 20, 30)
for coord in coordenadas:
    print(coord)

colores = {"rojo", "verde", "azul"}
for color in colores:
    print(color)  # Orden no garantizado