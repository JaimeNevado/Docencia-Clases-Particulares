import libreriaIA as ia

enlace = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg/1200px-A6-EDY_A380_Emirates_31_jan_2013_jfk_%288442269364%29_%28cropped%29.jpg"
respuesta = ia.analizarImagen(enlace)

print(respuesta)

ia.generarImagen(respuesta)