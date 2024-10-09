#include <iostream>

// Definición de la estructura del nodo de la lista enlazada
struct Nodo
{
	int dato;		 // Dato que contiene el nodo
	Nodo *siguiente; // Puntero al siguiente nodo
};

// Clase para la lista enlazada
class Cola
{
private:
	Nodo *frente; // al principio
	Nodo *final;  // al final
	int tamaño;

public:
	// Constructor para inicializar la lista vacía
	Cola()
	{
		frente = nullptr;
		final = nullptr;
		tamaño = 0;
	}

	// Destructor para liberar la memoria de los nodos
	~Cola()
	{
		// Por completar por Maikel
	}
};

// Función principal
int main()
{
	Cola lista;

	// Insertar nodos para crear una lista ordenada
	lista.insertar(1);
	lista.insertar(4);
	lista.insertar(6);
	lista.insertar(7);
	lista.insertar(8);

	// Mostrar la lista inicial
	std::cout << "Lista inicial: ";
	lista.mostrar();

	// Insertar un nodo en orden
	lista.insertar(5);

	// Mostrar la lista después de insertar
	std::cout << "Lista después de insertar 5: ";
	lista.mostrar();

	int variable = lista.getTamaño();

	std::cout << "El tamaño es: " << variable << std::endl;

	return 0;
}
