def verificar_radio_positivo(radio):
    if radio <= 0:
        return False
    else:
        return True

def calcular_area_circulo(radio):
    if verificar_radio_positivo(radio):
        area = 3.14 * radio ** 2
    else:
        print("Error: El radio debe ser un número positivo.")
        area = -1
    return area

# Ejemplo de uso:
radio_usuario = float(input("Ingrese el radio del círculo: "))
area_circulo = calcular_area_circulo(radio_usuario)

if area_circulo > 0:
    print("El área del círculo con radio",radio_usuario,  "es:", area_circulo)
