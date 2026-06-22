import turtle

# Configuro la pantalla, que se le puede poner el titulo o el color que se quiera
pantalla = turtle.Screen()
pantalla.title("Patrones con Tortuguita")
pantalla.bgcolor("black")

# Configuración de la tortuguita porque ha evolucionado, y le metemos la vel maxima.
# width es el grosor del lapiz de la tortuga.
t = turtle.Turtle()
t.speed(0)
t.color("yellow")
t.width(2)

# le dibujo que para i se repita en bucle en este caso 36 veces en forma de cuadrado
# _ es un valor de variable cualquiera pero en realidad no lo vas a usar, sobretodo dicho en 'for'
# t igualmente es el nombre de una variable y lo encuadra a donde quiero (a dcha, izquda, donde sea)
for i in range(36):
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

turtle.done()