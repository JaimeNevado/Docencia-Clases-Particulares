nombre1 = "Damian"
edad1 = 19
altura1 = 1.78

nombre2 = "Raul"
edad2 = 20
altura2 = 1.98

listaPersonas = ["Damian", 19, 1.78, "Raul", 20, 1.98]

diccionarioPersona1 = {
	"nombre" : "Damian",
	"edad" : 19,
	"altura" : 1.78
}

diccionarioPersona2 = {
	"nombre" : "Raul",
	"edad" : 20,
	"altura" : 1.98
}

lista = [
	diccionarioPersona1,
	diccionarioPersona2
]


print(lista[0]["nombre"])
print(lista[1]["nombre"])