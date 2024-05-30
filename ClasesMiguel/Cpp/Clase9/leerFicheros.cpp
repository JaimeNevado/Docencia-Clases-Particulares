#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream archivo; // declaramos el archivo de entrada
	char letra;

	archivo.open("maikel.txt"); // Abrimos el archivo "prueba.txt" en modo lectura

	if (!archivo)
	{ // Verificamos si se pudo abrir el archivo correctamente
		cout << "El archivo no existe";
	}
	else
	{
		archivo.get(letra); // Hacemos una primera lectura para detectar el final del archivo

		while (!archivo.eof())
		{				   // Leer hasta el final del archivo
			cout << letra; // Imprimimos el caracter leído

			archivo.get(letra); // Leemos el siguiente caracter
		}
	}

	// El archivo se cierra automáticamente al salir del ámbito de la variable "archivo"
	return 0;
}
