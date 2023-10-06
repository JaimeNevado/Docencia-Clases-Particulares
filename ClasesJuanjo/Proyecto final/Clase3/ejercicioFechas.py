from datetime import datetime

# Solicita al usuario ingresar el año, mes y día
year = input("Ingresa el año (ejemplo: 2023): ")
month = input("Ingresa el mes (1-12): ")
day = input("Ingresa el día (1-31): ")

# Crea un objeto datetime con la fecha ingresada por el usuario
fecha_str = f"{year}-{month}-{day}"
fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

# Obtiene el nombre del día de la semana correspondiente
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombre_dia_semana = dias_semana[fecha.weekday()]

# Imprime el día de la semana
print(f"El {day}/{month}/{year} es un {nombre_dia_semana}.")
