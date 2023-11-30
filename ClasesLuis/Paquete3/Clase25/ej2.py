def verificarEdad(edad):
    if edad >= 18:
        return "Mayor de edad"
    elif edad <= 0:
        return "error"
    else:
        return "Menor de edad" 

# Prueba de la función (Main)

print(verificarEdad(13))
print(verificarEdad(20))
