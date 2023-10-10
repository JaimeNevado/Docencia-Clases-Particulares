import random

numero_secreto = random.randint(1, 10)
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza < numero_secreto:
        print("Más alto. Intenta de nuevo.")
    elif adivinanza > numero_secreto:
        print("Más bajo. Intenta de nuevo.")
print("¡Correcto! ¡Has adivinado el número secreto.")
