#include <iostream>

// Definición de la estructura del nodo de la lista doblemente enlazada
struct Nodo
{
	int dato;		 // Dato que contiene el nodo
	Nodo *anterior;	 // Puntero al nodo anterior
	Nodo *siguiente; // Puntero al siguiente nodo

	Nodo(int valor) : dato(valor), anterior(nullptr), siguiente(nullptr) {}
};

// Clase para la lista doblemente enlazada
class ListaDoblementeEnlazada
{
private:
	Nodo *cabeza; // Puntero al primer nodo de la lista
	Nodo *cola;	  // Puntero al último nodo de la lista

public:
	// Constructor para inicializar la lista vacía
	ListaDoblementeEnlazada() : cabeza(nullptr), cola(nullptr) {}

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
		Nodo *nuevoNodo = new Nodo(dato); // Crear un nuevo nodo
		nuevoNodo->siguiente = cabeza;	  // El siguiente nodo del nuevo nodo es el actual cabeza

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
		Nodo *nuevoNodo = new Nodo(dato); // Crear un nuevo nodo

		if (cola != nullptr)
		{
			cola->siguiente = nuevoNodo; // El nodo actual cola apunta al nuevo nodo como siguiente
			nuevoNodo->anterior = cola;	 // El nodo anterior del nuevo nodo es el actual cola
		}
		else
		{
			cabeza = nuevoNodo; // Si la lista estaba vacía, cabeza también debe apuntar al nuevo nodo
		}

		cola = nuevoNodo; // Actualizar cola para que apunte al nuevo nodo
	}

	// Función para mostrar los elementos de la lista en orden directo
	void mostrarAdelante() const
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
	void mostrarAtras() const
	{
		Nodo *actual = cola;
		while (actual != nullptr)
		{
			std::cout << actual->dato << " ";
			actual = actual->anterior;
		}
		std::cout << std::endl;
	}

	// Función para obtener el tamaño de la lista
	int tamaño() const
	{
		int tamaño = 0;
		Nodo *actual = cabeza;
		while (actual != nullptr)
		{
			tamaño++;
			actual = actual->siguiente;
		}
		return tamaño;
	}

	// Función para obtener la cabeza de la lista
	Nodo *getCabeza() const
	{
		return cabeza;
	}
};

// Función para sumar dos listas doblemente enlazadas
ListaDoblementeEnlazada sumarListas(const ListaDoblementeEnlazada &a, const ListaDoblementeEnlazada &b)
{
	ListaDoblementeEnlazada resultado;

	if (a.tamaño() == b.tamaño())
	{
		Nodo *actualA = a.getCabeza();
		Nodo *actualB = b.getCabeza();

		while (actualA != nullptr && actualB != nullptr)
		{
			resultado.insertarAlFinal(actualA->dato + actualB->dato);
			actualA = actualA->siguiente;
			actualB = actualB->siguiente;
		}
	}
	else
	{
		std::cerr << "Error: Las listas tienen tamaños diferentes." << std::endl;
	}

	return resultado;
}

// Función principal
int main()
{
	ListaDoblementeEnlazada lista1;
	ListaDoblementeEnlazada lista2;

	// Insertar nodos al comienzo de la lista
	lista1.insertarAlComienzo(10);
	lista1.insertarAlComienzo(20);
	lista1.insertarAlComienzo(30);

	// Insertar nodos al comienzo de la lista
	lista2.insertarAlComienzo(10);
	lista2.insertarAlComienzo(20);
	lista2.insertarAlComienzo(30);

	std::cout << "Lista 1: ";
	lista1.mostrarAdelante();
	std::cout << "Lista 2: ";
	lista2.mostrarAdelante();

	ListaDoblementeEnlazada sol = sumarListas(lista1, lista2);

	std::cout << "Lista resultado: ";
	sol.mostrarAdelante();

	return 0;
}
