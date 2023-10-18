print("¡Bienvenido al programa de lanzamiento de cohetes!")

energia_encendida = int(input("¿El sistema de energía está encendido? (Seleccione 1 para sí, 0 para no): "))

if energia_encendida == 1:
    motores_listos = int(input("¿Los motores están listos? (Seleccione 1 para sí, 0 para no): "))
    if motores_listos == 1:
        tripulacion_abordo = int(input("¿La tripulación está abordo? (Seleccione 1 para sí, 0 para no): "))
        if tripulacion_abordo == 1:
            print("Despegue aprobado, lanzando cohete")
        else:
            print("ERROR: La tripulación no está")
    else:
        print("ERROR: Los motores están apagados")
else:
    print("ERROR: El sistema de energía está apagado")

