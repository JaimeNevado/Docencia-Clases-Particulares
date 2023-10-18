contador = 0
sumaNotas = 0
personas = int(input("Dime cuantos alumnos: "))
#personas = 500

while (contador < personas):
    nota = int(input("Dime una nota: "))
    if(nota<=10 and nota>=0):
        sumaNotas = sumaNotas + nota
    else:
        print("Estas haciendo trampa")
        contador = personas
        sumaNotas = 0
    contador = contador + 1

media = sumaNotas / personas
print("La media es: ", media)