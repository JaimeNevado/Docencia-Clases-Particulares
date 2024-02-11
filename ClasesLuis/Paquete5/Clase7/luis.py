def comprobarMenor100(m1):
    for i in range (len(m1)):
        for j in range (len(m1)):
            if m1[i][j] < 0 or  m1[i][j] > 100:
                return False
    return True


def sumarmatriz(m1):
    suma = 0
    for i in range (len(m1)):
        for j in range (len(m1)):
            suma = suma + m1[i][j]
    condicion = True
    if suma != 300 :
        condicion = False
    return condicion
    

Ejemplo1 = [
    [20, 30, 50],
    [50, 0, 50],
    [30, 70, 0]
]

retorno = comprobarMenor100(Ejemplo1)
retorno2 = sumarmatriz(Ejemplo1)


if retorno == True and retorno2 == True:
    print("La matriz SI cumple la condicion")
else:
	print("La matriz NO cumple la condicion")
    
