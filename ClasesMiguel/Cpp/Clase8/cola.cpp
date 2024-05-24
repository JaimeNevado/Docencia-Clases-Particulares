#include <iostream>

// Definición de la estructura del nodo de la cola
struct Nodo
{
	int dato;		 // Dato que contiene el nodo
	Nodo *siguiente; // Puntero al siguiente nodo
};

// Clase para la cola
class Cola
{
private:
	Nodo *frente; // Puntero al primer nodo de la cola (frente)
	Nodo *final;  // Puntero al último nodo de la cola (final)
	int tamano;	  // Tamaño de la cola

public:
	// Constructor para inicializar la cola vacía
	Cola()
	{
		frente = nullptr;
		final = nullptr;
		tamano = 0;
	}

	// Destructor para liberar la memoria de los nodos
	~Cola()
	{
		while (!isEmpty())
		{
			desencolar();
		}
	}

	// Función para encolar (añadir un elemento al final de la cola)
	void encolar(int dato)
	{
		Nodo *nuevoNodo = new Nodo;		// Crear un nuevo nodo
		nuevoNodo->dato = dato;			// Asignar el dato al nodo
		nuevoNodo->siguiente = nullptr; // El nuevo nodo no tiene siguiente nodo

		if (isEmpty())
		{
			frente = nuevoNodo; // Si la cola está vacía, el nuevo nodo es el frente
		}
		else
		{
			final->siguiente = nuevoNodo; // Si no, el último nodo actual apunta al nuevo nodo
		}

		final = nuevoNodo; // Actualizar el final para que apunte al nuevo nodo
		tamano++;		   // Incrementar el tamaño de la cola
	}

	// Función para desencolar (eliminar un elemento del inicio de la cola)
	void desencolar()
	{
		if (isEmpty())
		{
			std::cout << "La cola está vacía, no se puede desencolar.\n";
			return;
		}

		Nodo *temp = frente;		// Guardar el nodo que se va a eliminar
		frente = frente->siguiente; // Actualizar el frente para que apunte al siguiente nodo

		if (frente == nullptr)
		{
			final = nullptr; // Si la cola queda vacía, actualizar final a nullptr
		}

		delete temp; // Liberar la memoria del nodo eliminado
		tamano--;	 // Decrementar el tamaño de la cola
	}

	// Función para obtener el elemento del frente de la cola sin eliminarlo
	int front()
	{
		if (isEmpty())
		{
			std::cerr << "La cola está vacía.\n";
			return -1; // Valor de error, ya que la cola está vacía
		}

		return frente->dato; // Devolver el dato del nodo en el frente
	}

	// Función para chequear si la cola está vacía
	bool isEmpty()
	{
		return frente == nullptr; // La cola está vacía si frente es nullptr
	}

	// Función para obtener el tamaño de la cola
	int size()
	{
		return tamano; // Devolver el tamaño de la cola
	}
};

// Función principal
int main()
{
	Cola cola;

	// Encolar elementos en la cola
	cola.encolar(10);
	cola.encolar(20);
	cola.encolar(30);

	// Obtener y mostrar el elemento del frente sin eliminarlo
	std::cout << "Frente de la cola: " << cola.front() << std::endl;

	// Desencolar un elemento
	cola.desencolar();
	std::cout << "Después de desencolar, frente de la cola: " << cola.front() << std::endl;

	// Mostrar el tamaño de la cola
	std::cout << "Tamaño de la cola: " << cola.size() << std::endl;

	// Desencolar todos los elementos restantes
	cola.desencolar();
	cola.desencolar();
	std::cout << "Después de desencolar todos los elementos, ¿la cola está vacía? " << (cola.isEmpty() ? "Sí" : "No") << std::endl;

	return 0;
}
