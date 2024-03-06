preguntas = ("¿Cuántos elementos hay en la tabla periódica?: ",
             "¿Qué animal pone los huevos más grandes?: ",
             "¿Cuál es el gas más abundante en la atmósfera de la Tierra?: ",
             "¿Cuántos huesos hay en el cuerpo humano?: ",
             "¿Qué planeta en el sistema solar es el más caliente?: ")

opciones = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Ballena", "B. Cocodrilo", "C. Elefante", "D. Avestruz"),
            ("A. Nitrógeno", "B. Oxígeno", "C. Dióxido de Carbono", "D. Hidrógeno"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercurio", "B. Venus", "C. Tierra", "D. Marte"))

respuestas = ("C", "D", "A", "A", "B")
respuestas_usuario = []
puntuacion = 0
numero_pregunta = 0

for pregunta in preguntas:
    print("----------------------")
    print(pregunta)
    for opcion in opciones[numero_pregunta]:
        print(opcion)

    respuesta_usuario = input("Ingrese (A, B, C, D): ").upper()
    respuestas_usuario.append(respuesta_usuario)
    if respuesta_usuario == respuestas[numero_pregunta]:
        puntuacion += 20
        print("¡CORRECTO!")
    else:
        print("¡INCORRECTO!")
        print(f"{respuestas[numero_pregunta]} es la respuesta correcta")
    numero_pregunta += 1

print("----------------------")
print("       RESULTADOS     ")
print("----------------------")

print("Respuestas del usuario: ", end="")
for respuesta_usuario in respuestas_usuario:
    print(respuesta_usuario, end=" ")
print()

print(f"Tu puntuacion es: {puntuacion}%")
