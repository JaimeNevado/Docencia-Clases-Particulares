import os

def comprobar_permisos(nombre_archivo, permiso):
    if permiso == 'r':
        estado = os.access(nombre_archivo, os.R_OK)
        permiso = "lectura"
    elif permiso == 'w':
        estado = os.access(nombre_archivo, os.W_OK)
        permiso = "escritura"
    else:
        print("Permiso indefinido")

    if estado:
        print(f"El archivo {nombre_archivo} tiene permiso de {permiso}.")
    else:
        print(f"El archivo {nombre_archivo} no tiene permiso de {permiso}.")

archivo = input("Ingresa el nombre del archivo: ")
permiso = input("Ingresa el permiso a verificar (r/w): ")

if os.access(archivo, os.F_OK):
    comprobar_permisos(archivo, permiso)
else:
    print("El archivo no existe")