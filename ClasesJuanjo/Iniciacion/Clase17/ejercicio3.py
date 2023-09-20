def calcularAreaBase(radio):
    areaCirculo = 3.14 * radio * radio
    return areaCirculo

def calcularCilindro(altura, radio):
    # Cálculo del volumen del cilindro
    volumenCilindro = calcularAreaBase(radio) * altura
    return volumenCilindro

def calcularPiramide(altura, radio):
    # Cálculo del volumen de la pirámide
    volumenPiramide = (calcularAreaBase(radio) * altura) / 3
    return volumenPiramide

def calcularVolumen(tipo_figura, altura, radio):
    if tipo_figura == "cilindro":
        volumen = calcularCilindro(altura, radio)
    elif tipo_figura == "piramide":
        volumen = calcularPiramide(altura, radio)
    else:
        print("Tipo de figura no válido")
    return volumen


figura = "cilindro"
volumen = calcularVolumen(figura, 10, 4)
print("El volumen es: ", volumen)