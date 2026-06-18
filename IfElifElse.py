# If = 'si pasa esto...'
# Efil = 'si no pasó lo anterior pero pasa esto otro..'
# Else = 'si nada de lo anterior pasó...'

nota = 75

if nota >= 90:
    calificacion = "A"
elif nota >= 80:
    calificacion = "B"
elif nota >= 70:
    calificacion = "C"
elif nota >= 60:
    calificacion = "D"
else:
    calificacion = "F"

print(f"Tu calificación es: {calificacion}")
# Output: Tu calificación es: C