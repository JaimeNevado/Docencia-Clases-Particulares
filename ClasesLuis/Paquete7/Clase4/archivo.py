import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Formatear la fecha y hora actual hasta los segundos
fecha_hora_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")

# Imprimir la fecha y hora formateada
print("La fecha y hora actual formateada es:", fecha_hora_formateada)
