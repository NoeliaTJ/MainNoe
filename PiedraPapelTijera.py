# importamos random para el que ordenador pueda elegir al azar
import random

# Estas son las tres opciones validas en este caso de este juego
opciones = ("piedra", "papel", "tijera")

# y lo que le decimos que muestre en pantalla
print("Juego: Piedra, papel o tijera")
print("Escribe 'salir' para terminar.\n")

# le pedimos las condicionales mientras v o f
while True:
    usuario = input("Elige piedra, papel o tijera: ").lower()

# Si el usuario quiere salir, acabamos el juego
    if usuario == "salir":
        print("Gracias por jugar 😊")
        break
# Aqui comprobamos que la opcion del usuario es valida.
    if usuario not in opciones:
        print("Opción no válida, prueba otra vez.\n")
        continue
# Nuestro amigo ordenador elige una opcion de las tres que le hemos dado arriba
# la | en este caso solo es visual
    ordenador = random.choice(opciones)
    print(f"Tú: {usuario} | Ordenador: {ordenador}")

# Y aquí se comparan las opciones para decidir el resultado
# la \n es un salto de línea
# los == igualan el resultado
    if usuario == ordenador:
        print("Empate.\n")
    elif (
        (usuario == "piedra" and ordenador == "tijera") or
        (usuario == "papel" and ordenador == "piedra") or
        (usuario == "tijera" and ordenador == "papel")
    ):
        print("¡Has ganado!\n")
    else:
        print("Ha ganado el ordenador.\n")