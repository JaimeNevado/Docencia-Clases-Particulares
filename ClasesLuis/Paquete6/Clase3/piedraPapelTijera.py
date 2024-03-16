def escribir_opciones():
    print("PIEDRA, PAPEL , TIJERA")



jugador1 = input("Dime el nombre del jugador 1: ").capitalize()
jugador2 = input("Dime el nombre del jugador 2: ").capitalize()
escribir_opciones()
opcion1 = input(f"{jugador1} , que opcion eliges? ").lower()
opcion2 = input(f"{jugador2} , que opcion eliges? ").lower()


if opcion1 == "piedra":
    if opcion2 == "piedra":
        print("Empate")
    elif opcion2 == "tijeras":
        print(f"Gana {jugador1}")
    elif opcion2 == "papel":
        print(f"Gana {jugador2}")
    else:
        print("Revise la eleccion")
elif opcion1 == "papel":
    if opcion2 == "papel":
        print("Empate")
    elif opcion2 == "tijeras":
        print(f"Gana {jugador2}")
    elif opcion2 == "piedra":
        print(f"Gana {jugador1}")
    else:
        print("Revise la eleccion")
elif opcion1 == "tijera":
    if opcion2 == "tijera":
        print("Empate")
    elif opcion2 == "papel":
        print(f"Gana {jugador1}")
    elif opcion2 == "piedra":
        print(f"Gana {jugador2}")
    else:
        print("Revise la eleccion")
else:
    print("Hay un error , por favor , revise la palabra")