import matplotlib.pyplot as plt
import json

archivo= open("datos.json","r")
lineas= json.load(archivo)

# Bucle para buscar las provincias
provincias = []
for elemento in lineas:
    if elemento["province"] not in provincias:
        provincias.append(elemento["province"])

def sumar_valores(provincia, buscar):
    valor = 0
    for elemento in lineas:
        if (elemento["province"] == provincia):
            valor = valor + int(elemento[buscar])
    return valor

# Máximo
def provincia_maxima(buscar):
    numero_max = -1
    for provincia in provincias:
        if sumar_valores(provincia, buscar) > numero_max:
            provincia_max = provincia
            numero_max = sumar_valores(provincia, buscar)
    return provincia_max

# Mínimo
def provincia_min(buscar):
    numero_min = 99999
    for provincia in provincias:
        if sumar_valores(provincia, buscar) < numero_min:
            provincia_min = provincia
            numero_min = sumar_valores(provincia, buscar)
    return provincia_min

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))

    if opcion == 1:
        etiquetas = provincias
        valores = []
        for provincia in provincias:
            valor = sumar_valores(provincia, "num_def")
            valores.append(valor)

        print("La provincia con mayor número de defunciones es: ", provincia_maxima("num_def"))
        print("La provincia con menor número de defunciones es: ", provincia_min("num_def"))

        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title(f'Número de Defunciones')
        plt.show()
    elif opcion==2:
        etiquetas = provincias
        valores = []
        for provincia in provincias:
            valor = sumar_valores(provincia, "new_cases")
            valores.append(valor)

        print("La provincia con mayor número de casos es: ", provincia_maxima("new_cases"))
        print("La provincia con menor número de casos es: ", provincia_min("new_cases"))

        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title(f'Número de Casos')
        plt.show()
    elif opcion==3:
        etiquetas = provincias
        valores = []
        for provincia in provincias:
            valor = sumar_valores(provincia, "num_hosp")
            valores.append(valor)

        print("La provincia con mayor número de casos es: ", provincia_maxima("num_hosp"))
        print("La provincia con menor número de casos es: ", provincia_min("num_hosp"))

        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title(f'Número de Hospitalizados')
        plt.show()
    elif opcion==4:
        etiquetas = provincias
        valores = []
        for provincia in provincias:
            valor = sumar_valores(provincia, "num_uci")
            valores.append(valor)

        print("La provincia con mayor número de casos es: ", provincia_maxima("num_uci"))
        print("La provincia con menor número de casos es: ", provincia_min("num_uci"))

        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title(f'Número de UCI')
        plt.show()
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
