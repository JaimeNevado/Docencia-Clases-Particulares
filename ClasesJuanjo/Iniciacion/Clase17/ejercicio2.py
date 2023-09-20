def calcularArea(radio):
    areaCirculo = 3.14 * radio * radio
    return areaCirculo

def calcularVolumen(altura, radio):
    volumenCilindro = altura * calcularArea(radio)
    return volumenCilindro

altura = 7
radio = 3
volumen = calcularVolumen(altura, radio)
print("El volumen del cilindro es:", volumen)
