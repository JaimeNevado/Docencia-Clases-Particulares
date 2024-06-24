#include <iostream>
#include "misFunciones.h"

// Función para generar una lista con 1000 elementos en orden ascendente
ListaEnlazada generarListaAscendente(int tam)
{
	ListaEnlazada lista;
	for (int i = 0; i < tam; ++i)
	{
		lista.insertarAlFinal(i * 2 + 1); // Añadir números impares: 1, 3, 5, 7, ...
	}
	return lista;
}

int algoritmo(int &edad)
{
	edad = 19;
	return 0;
}

int main()
{
	ListaEnlazada lista = generarListaAscendente(1000);

	int edad = 88;
	algoritmo(edad);

	std::cout << edad << std::endl;
	return 0;
}
