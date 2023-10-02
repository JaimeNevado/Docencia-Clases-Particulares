import csv 

datos_filtrados = [] 
archivo = open("prueba.csv", "r")
lineas = csv.DictReader(archivo) 
for fila in lineas:
    provincia = fila['province']
    num_def = int(fila['num_def'])
    new_cases = int(fila['new_cases'])
        
    # Crear un diccionario con las columnas seleccionadas
    datos_seleccionados = {
        'province': provincia,
        'num_def': num_def,
        'new_cases': new_cases
    }
        
    # Agregar el diccionario a la lista de datos filtrados
    datos_filtrados.append(datos_seleccionados)
print(datos_filtrados)

