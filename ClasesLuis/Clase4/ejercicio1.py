calificacion = float(input("Ingresa tu calificación: "))

# Calificacion = -4 7 10 3 2
if calificacion >= 5.0:
    # 7 10
    print("Aprobado")
else:
    # -4 3 2
    if (calificacion < 0):
        # -4
        print("error")
    else:
        # 3 2
        print("Suspenso")
