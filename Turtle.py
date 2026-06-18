import turtle  # Importa la librería

t = turtle.Turtle()  # Crea la “tortuga”

# Dibujar un cuadrado
for _ in range(4):
    t.forward(100)  # Avanza 100 pasos
    t.right(90)     # Gira 90 grados a la derecha

turtle.done()  # Mantiene la ventana abierta
