from datetime import datetime

# Fecha en formato AAAA-MM-DD
fecha_str = "2021-01-28"

# Convierte la fecha a un objeto datetime
fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")

# Obtiene el día de la semana como un número (0=Lunes, 1=Martes, ..., 6=Domingo)
numero_dia_semana = fecha_obj.weekday()

# Convierte el número del día de la semana a su nombre
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombre_dia_semana = dias_semana[numero_dia_semana]

print("Fecha:", fecha_str)
print("Número del día de la semana:", numero_dia_semana)
print("Nombre del día de la semana:", nombre_dia_semana)
