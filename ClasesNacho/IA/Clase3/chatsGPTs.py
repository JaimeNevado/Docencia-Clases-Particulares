import libreriaIA as ia

pregunta = "dime que tienen de diferente estas dos personas"
e1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/John_F._Kennedy%2C_White_House_color_photo_portrait.jpg/1200px-John_F._Kennedy%2C_White_House_color_photo_portrait.jpg"
e2 = "https://cdn.britannica.com/19/101219-050-A07A26EF/Barack-Obama.jpg"

#texto = ia.analizarVariasImagenes(pregunta, e1, e2)

r2 = "Empieza una concersacion"
i = 0
while (True):
	print("Iteracion nº ", i)
	i = i + 1
	r1 = ia.chatGPT(r2, "Cuando quieras terminar de hablar, escribe solamente la palabra FINISH, sin nada mas")
	print(r1)
	if (r1 == "FINISH"):
		break

	r2 = ia.chatGPT(r1, "Cuando quieras terminar de hablar, escribe solamente la palabra FINISH, sin nada mas")
	print(r2)

	if (r2 == "FINISH"):
		break
