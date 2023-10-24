# Eliminar espacios en blanco al principio y al final de una cadena y luego encontrar la longitud de la cadena resultante.
my_string = "   Esto es un ejemplo de cadena con espacios   "
stripped_string = my_string.strip()
length_original = len(my_string)
length_stripped = len(stripped_string)

print(f"Cadena original: '{my_string}'")
print(f"Cadena sin espacios en blanco: '{stripped_string}'")
print(f"Longitud de la cadena original: {length_original}")
print(f"Longitud de la cadena sin espacios en blanco: {length_stripped}")
