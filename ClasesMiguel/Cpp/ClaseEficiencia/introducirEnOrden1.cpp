#include <iostream>
#include "listaEnlazada.h"

using namespace std;

// O(N)

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

int insertarEnOrden(ListaEnlazada &lista, int elemento)
{
	int i = 0;
	int numIteraciones = 0;

	// Avanzar el iterador hasta la posición adecuada
	while (i < lista.getTamaño() && lista.obtenerDatoEnPosicion(i) < elemento)
	{
		i++;
		numIteraciones++;
	}

	lista.insertarEnPosicion(i, elemento); // Insertar el elemento en la posición encontrada
	return numIteraciones;
}

int main()
{
	ListaEnlazada lista = generarListaAscendente(1000);
	int elemento = 462;

	int vueltas = insertarEnOrden(lista, elemento);

	// lista.mostrar();

	cout << "Ha dado: " << vueltas << " vueltas" << endl;

	return 0;
}
