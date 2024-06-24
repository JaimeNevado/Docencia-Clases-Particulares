#include <iostream>

// Definición de la estructura del nodo de la lista enlazada
struct Nodo
{
	int dato;		 // Dato que contiene el nodo
	Nodo *siguiente; // Puntero al siguiente nodo
};

// Clase para la lista enlazada
class ListaEnlazada
{
private:
	Nodo *cabeza; // Puntero al primer nodo de la lista
	int tamaño;

public:
	// Constructor para inicializar la lista vacía
	ListaEnlazada()
	{
		tamaño = 0;
		cabeza = nullptr;
	}

	// Destructor para liberar la memoria de los nodos
	~ListaEnlazada()
	{
		Nodo *actual = cabeza;
		while (actual != nullptr)
		{
			Nodo *siguiente = actual->siguiente;
			delete actual;
			actual = siguiente;
		}
	}

	// Función para insertar un nodo al comienzo de la lista
	void insertarAlComienzo(int dato)
	{
		Nodo *nuevoNodo = new Nodo;	   // Crear un nuevo nodo
		nuevoNodo->dato = dato;		   // Asignar el dato al nodo
		nuevoNodo->siguiente = cabeza; // El siguiente nodo del nuevo nodo es el actual cabeza
		cabeza = nuevoNodo;			   // Actualizar cabeza para que apunte al nuevo nodo
		tamaño++;
	}

	// Función para insertar un nodo al final de la lista
	void insertarAlFinal(int dato)
	{
		Nodo *nuevoNodo = new Nodo;		// Crear un nuevo nodo
		nuevoNodo->dato = dato;			// Asignar el dato al nodo
		nuevoNodo->siguiente = nullptr; // El nuevo nodo es el último, así que su siguiente es nullptr

		if (cabeza == nullptr)
		{
			cabeza = nuevoNodo; // Si la lista estaba vacía, cabeza también debe apuntar al nuevo nodo
		}
		else
		{
			Nodo *actual = cabeza;
			while (actual->siguiente != nullptr)
			{
				actual = actual->siguiente; // Avanzar al último nodo en la lista
			}
			actual->siguiente = nuevoNodo; // Enlazar el último nodo al nuevo nodo
		}
		tamaño++;
	}

	// Función para eliminar un nodo de la lista
	void eliminarNodo(int dato)
	{
		Nodo *actual = cabeza;
		Nodo *anterior = nullptr;

		// Buscar el nodo con el dato especificado
		while (actual != nullptr && actual->dato != dato)
		{
			anterior = actual;
			actual = actual->siguiente;
		}

		if (actual == nullptr)
		{
			std::cout << "Nodo con el dato " << dato << " no encontrado.\n";
			return; // Si no se encuentra el nodo, salir de la función
		}

		if (anterior != nullptr)
		{
			anterior->siguiente = actual->siguiente; // Actualizar el siguiente del nodo anterior
		}
		else
		{
			cabeza = actual->siguiente; // Si se elimina el primer nodo, actualizar cabeza
		}

		delete actual; // Liberar la memoria del nodo eliminado
		tamaño--;
	}

	// Función para mostrar los elementos de la lista
	void mostrar()
	{
		Nodo *actual = cabeza;
		while (actual != nullptr)
		{
			std::cout << actual->dato << " ";
			actual = actual->siguiente;
		}
		std::cout << std::endl;
	}

	// Función para insertar un nodo en orden
	void insertarEnOrden(int dato)
	{
		Nodo *nuevoNodo = new Nodo; // Crear un nuevo nodo
		nuevoNodo->dato = dato;
		nuevoNodo->siguiente = nullptr;

		if (cabeza == nullptr || cabeza->dato >= dato)
		{
			// Insertar al comienzo si la lista está vacía o si el dato es menor o igual al primer nodo
			if (cabeza != nullptr && cabeza->dato == dato)
			{
				delete nuevoNodo; // El dato ya está presente, no se inserta
				return;
			}
			nuevoNodo->siguiente = cabeza;
			cabeza = nuevoNodo;
		}
		else
		{
			Nodo *actual = cabeza;
			while (actual->siguiente != nullptr && actual->siguiente->dato < dato)
			{
				actual = actual->siguiente; // Avanzar al siguiente nodo mientras sea menor que el dato
			}
			if (actual->siguiente != nullptr && actual->siguiente->dato == dato)
			{
				delete nuevoNodo; // El dato ya está presente, no se inserta
				return;
			}
			nuevoNodo->siguiente = actual->siguiente;
			actual->siguiente = nuevoNodo;
		}
		tamaño++;
	}

	int getTamaño()
	{
		return tamaño;
	}

	// HACER EN CLASE
	// Función para añadir un nodo en la posición X
	void insertarEnPosicion(int dato, int posicion)
	{
		if (posicion < 0 || posicion > tamaño)
		{
			std::cout << "Posición invalida broo\n";
			return;
		}

		Nodo *nuevoNodo = new Nodo;
		nuevoNodo->dato = dato;

		if (posicion == 0)
		{
			// Insertar al comienzo
			nuevoNodo->siguiente = cabeza;
			cabeza = nuevoNodo;
		}
		else
		{
			Nodo *actual = cabeza;
			int contador = 0;
			while (contador < posicion - 1)
			{
				actual = actual->siguiente;
				contador++;
			}
			nuevoNodo->siguiente = actual->siguiente;
			actual->siguiente = nuevoNodo;
		}
		tamaño++;
	}

	// HACER EN CLASE!!
	// Función para obtener el dato en la posición X de la lista
	int obtenerDatoEnPosicion(int posicion)
	{
		int datoADevolver = 0;
		if (posicion < 0 || posicion >= tamaño)
		{
			std::cerr << "Error: Posición invalida brooo\n";
			return -1;
		}

		Nodo *actual = cabeza;
		int contador = 0;

		while (contador < posicion)
		{
			actual = actual->siguiente;
			contador++;
		}
		datoADevolver = actual->dato;

		return datoADevolver;
	}
};
