#include <iostream>

// Definición de la estructura del nodo de la lista doblemente enlazada
struct Nodo
{
	int dato;		 // Dato que contiene el nodo
	Nodo *anterior;	 // Puntero al nodo anterior
	Nodo *siguiente; // Puntero al siguiente nodo
};

// Clase para la lista doblemente enlazada
class ListaDoblementeEnlazada
{
private:
	Nodo *cabeza; // Puntero al primer nodo de la lista
	Nodo *cola;	  // Puntero al último nodo de la lista

public:
	// Constructor para inicializar la lista vacía
	ListaDoblementeEnlazada()
	{
		cabeza = nullptr;
		cola = nullptr;
	}

	// Destructor para liberar la memoria de los nodos
	~ListaDoblementeEnlazada()
	{
		Nodo *actual = cabeza;
		Nodo *siguiente;
		while (actual != nullptr)
		{
			siguiente = actual->siguiente;
			delete actual;
			actual = siguiente;
		}
	}

	// Función para insertar un nodo al comienzo de la lista
	void insertarAlComienzo(int dato)
	{
		Nodo *nuevoNodo = new Nodo;	   // Crear un nuevo nodo
		nuevoNodo->dato = dato;		   // Asignar el dato al nodo
		nuevoNodo->anterior = nullptr; // El nuevo nodo no tiene nodo anterior
		nuevoNodo->siguiente = cabeza; // El siguiente nodo del nuevo nodo es el actual cabeza

		if (cabeza != nullptr)
		{
			cabeza->anterior = nuevoNodo; // El nodo actual cabeza apunta al nuevo nodo como anterior
		}
		else
		{
			cola = nuevoNodo; // Si la lista estaba vacía, cola también debe apuntar al nuevo nodo
		}

		cabeza = nuevoNodo; // Actualizar cabeza para que apunte al nuevo nodo
	}

	// Función para insertar un nodo al final de la lista
	void insertarAlFinal(int dato)
	{
		Nodo *nuevoNodo = new Nodo;		// Crear un nuevo nodo
		nuevoNodo->dato = dato;			// Asignar el dato al nodo
		nuevoNodo->siguiente = nullptr; // El nuevo nodo no tiene siguiente nodo
		nuevoNodo->anterior = cola;		// El nodo anterior del nuevo nodo es el actual cola

		if (cola != nullptr)
		{
			cola->siguiente = nuevoNodo; // El nodo actual cola apunta al nuevo nodo como siguiente
		}
		else
		{
			cabeza = nuevoNodo; // Si la lista estaba vacía, cabeza también debe apuntar al nuevo nodo
		}

		cola = nuevoNodo; // Actualizar cola para que apunte al nuevo nodo
	}

	// Función para eliminar un nodo de la lista
	void eliminarNodo(int dato)
	{
		Nodo *actual = cabeza;

		while (actual != nullptr && actual->dato != dato)
		{
			actual = actual->siguiente; // Buscar el nodo con el dato especificado
		}

		if (actual == nullptr)
		{
			std::cout << "Nodo con el dato " << dato << " no encontrado.\n";
			return; // Si no se encuentra el nodo, salir de la función
		}

		if (actual->anterior != nullptr)
		{
			actual->anterior->siguiente = actual->siguiente; // Actualizar el siguiente del nodo anterior
		}
		else
		{
			cabeza = actual->siguiente; // Si se elimina el primer nodo, actualizar cabeza
		}

		if (actual->siguiente != nullptr)
		{
			actual->siguiente->anterior = actual->anterior; // Actualizar el anterior del siguiente nodo
		}
		else
		{
			cola = actual->anterior; // Si se elimina el último nodo, actualizar cola
		}

		delete actual; // Liberar la memoria del nodo eliminado
	}

	// Función para mostrar los elementos de la lista en orden directo
	void mostrarAdelante()
	{
		Nodo *actual = cabeza;
		while (actual != nullptr)
		{
			std::cout << actual->dato << " ";
			actual = actual->siguiente;
		}
		std::cout << std::endl;
	}

	// Función para mostrar los elementos de la lista en orden inverso
	void mostrarAtras()
	{
		Nodo *actual = cola;
		while (actual != nullptr)
		{
			std::cout << actual->dato << " ";
			actual = actual->anterior;
		}
		std::cout << std::endl;
	}
};

// Función principal
int main()
{
	ListaDoblementeEnlazada lista;

	// Insertar nodos al comienzo de la lista
	lista.insertarAlComienzo(10);
	lista.insertarAlComienzo(20);
	lista.insertarAlComienzo(30);

	// Insertar nodos al final de la lista
	lista.insertarAlFinal(40);
	lista.insertarAlFinal(50);

	// Mostrar la lista en orden directo
	std::cout << "Lista en orden directo: ";
	lista.mostrarAdelante();

	// Mostrar la lista en orden inverso
	std::cout << "Lista en orden inverso: ";
	lista.mostrarAtras();

	// Eliminar un nodo de la lista
	lista.eliminarNodo(20);
	std::cout << "Después de eliminar 20:\n";

	// Mostrar la lista nuevamente en orden directo
	std::cout << "Lista en orden directo: ";
	lista.mostrarAdelante();

	// Mostrar la lista nuevamente en orden inverso
	std::cout << "Lista en orden inverso: ";
	lista.mostrarAtras();

	return 0;
}
