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

public:
	// Constructor para inicializar la lista vacía
	ListaEnlazada()
	{
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
};

// Función principal
int main()
{
	ListaEnlazada lista;

	// Insertar nodos al comienzo de la lista
	lista.insertarAlComienzo(10);
	lista.insertarAlComienzo(20);
	lista.insertarAlComienzo(30);

	// Insertar nodos al final de la lista
	lista.insertarAlFinal(40);
	lista.insertarAlFinal(50);

	// Mostrar la lista
	std::cout << "Lista: ";
	lista.mostrar();

	// Eliminar un nodo de la lista
	lista.eliminarNodo(20);
	std::cout << "Después de eliminar 20:\n";

	// Mostrar la lista nuevamente
	std::cout << "Lista: ";
	lista.mostrar();

	return 0;
}
