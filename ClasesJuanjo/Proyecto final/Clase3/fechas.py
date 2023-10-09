from datetime import datetime


año=input("Escribe el año: ")
if(len(año) == 4):
	mes=input("Escribe el mes: ")
	if(len(mes)==2 and int(mes) > 0 and int(mes) <= 12):
		dia=input("Escribe el dia: ")
		if(len(dia)==2):
			fecha = f"{año}-{mes}-{dia}"
			print(fecha)
		else:
			print("Error, fecha en el día incorrecto")
	else:
		print("Error, fecha en mes incorrecto")
else:
		print("Error, fecha en el año incorrecto")

