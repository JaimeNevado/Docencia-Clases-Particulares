#include <iostream>
#include <fstream>
#include "listasEnlazadas.hpp"
using namespace std;

int main()
{
	ifstream archivo; // declaramos el archivo de entrada
	char letra;
	ListaEnlazada lista;

	archivo.open("maikel.txt"); // Abrimos el archivo "prueba.txt" en modo lectura

	if (!archivo)
	{ // Verificamos si se pudo abrir el archivo correctamente
		cout << "El archivo no existe";
	}
	else
	{
		archivo.get(letra); // Hacemos una primera lectura para detectar el final del archivo

		while (!archivo.eof())
		{ // Leer hasta el final del archivo
			if (letra != '\n')
			{
				lista.insertarAlFinal(letra - '0'); // Imprimimos el caracter leído
			}
			archivo.get(letra); // Leemos el siguiente caracter
		}
		lista.mostrar();
	}

	// El archivo se cierra automáticamente al salir del ámbito de la variable "archivo"
	return 0;
}
