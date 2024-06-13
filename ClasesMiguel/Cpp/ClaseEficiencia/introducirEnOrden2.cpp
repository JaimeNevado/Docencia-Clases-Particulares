#include <iostream>
#include "listaEnlazada.h"

using namespace std;

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

// Función para insertar un elemento en una lista ordenada utilizando búsqueda binaria
int insertarEnOrden(ListaEnlazada &lista, int elemento)
{
	int numIteraciones = 0;
	int ladoIzquierdo = 0;
	int ladoDerecho = lista.getTamaño();

	while (ladoIzquierdo < ladoDerecho)
	{
		int medio = ladoIzquierdo + (ladoDerecho - ladoIzquierdo) / 2;

		if (lista.obtenerDatoEnPosicion(medio) == elemento)
		{
			// Si encuentra el elemento igual, insertar después de él
			ladoIzquierdo = medio + 1;
			break;
		}
		else if (lista.obtenerDatoEnPosicion(medio) < elemento)
		{
			ladoIzquierdo = medio + 1;
		}
		else
		{
			ladoDerecho = medio;
		}

		numIteraciones++;
	}

	// Insertar el elemento en la posición ladoIzquierdo
	lista.insertarEnPosicion(elemento, ladoIzquierdo);

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
