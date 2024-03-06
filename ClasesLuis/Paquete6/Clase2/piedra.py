print("Bienvenido al juego Piedra, Papel, Tijera")
print("-----------------------------------------")

while True:
    jugador1 = input("Jugador 1, introduce tu elección (piedra, papel o tijera): ").lower()
    jugador2 = input("Jugador 2, introduce tu elección (piedra, papel o tijera): ").lower()

    if jugador1 not in ["piedra", "papel", "tijera"] or jugador2 not in ["piedra", "papel", "tijera"]:
        print("¡Opción no válida! Por favor, elige entre piedra, papel o tijera.")
        continue

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")

    jugar_nuevamente = input("¿Quieren jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente != "s":
        print("¡Gracias por jugar!")
        break
