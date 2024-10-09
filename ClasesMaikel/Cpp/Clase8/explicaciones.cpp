#include <iostream>
#include <string>

struct Nodo
{
	int dato;
	Nodo *siguiente;
};

class ListaEnlazada
{
private:
	Nodo *cabeza;

public:
	// constructor
	ListaEnlazada()
	{
		cabeza = nullptr;
	}
	void insertarAlComienzo(int numero)
	{
		Nodo *nuevoNodo = new Nodo;
		nuevoNodo->dato = numero;
		nuevoNodo->siguiente = cabeza;
		cabeza = nuevoNodo;
	}

	void eliminarNodo(int valor)
	{
		Nodo *actual = cabeza;
		Nodo *anterior = nullptr;

		while (actual != nullptr && actual->dato != valor)
		{
			anterior = actual;
			actual = actual->siguiente;
		}

		if (actual == nullptr)
		{
			std::cout << "No se ha encontrado el dato" << std::endl;
			return;
		}

		if (anterior == nullptr)
		{
			cabeza = actual->siguiente;
		}
		else
		{
			anterior->siguiente = actual->siguiente;
		}

		delete actual;
	}

	void mostrarLista(){
		
	}
};

int main()
{
	ListaEnlazada lista1;

	lista1.insertarAlComienzo(7);
	lista1.insertarAlComienzo(2);
	lista1.insertarAlComienzo(13);

	lista1.eliminarNodo(2);

	return 0;
}
