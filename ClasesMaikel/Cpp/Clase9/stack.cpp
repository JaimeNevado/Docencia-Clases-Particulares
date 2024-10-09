#include <iostream>

// Definición de la estructura del nodo de la pila
struct Node
{
	int data;	// Dato que contiene el nodo
	Node *next; // Puntero al siguiente nodo
};

// Clase para la pila
class Stack
{
private:
	Node *top; // Puntero al nodo en el tope de la pila

public:
	// Constructor para inicializar la pila vacía
	Stack() : top(nullptr) {}

	// Destructor para liberar la memoria de los nodos
	~Stack()
	{
		while (!isEmpty())
		{
			pop();
		}
	}

	// Función para insertar un elemento en el tope de la pila
	void push(int data)
	{
		Node *newNode = new Node; // Crear un nuevo nodo
		newNode->data = data;	  // Asignar el dato al nuevo nodo
		newNode->next = top;	  // El siguiente nodo del nuevo nodo es el actual tope de la pila
		top = newNode;			  // Actualizar top para que apunte al nuevo nodo
	}

	// Función para eliminar el elemento en el tope de la pila
	void pop()
	{
		if (!isEmpty())
		{
			Node *temp = top;
			top = top->next; // Mover el tope de la pila al siguiente nodo
			delete temp;	 // Liberar la memoria del nodo eliminado
		}
	}

	// Función para obtener el elemento en el tope de la pila
	int peek() const
	{
		if (!isEmpty())
		{
			return top->data;
		}
		throw std::out_of_range("La pila está vacía");
	}

	// Función para verificar si la pila está vacía
	bool isEmpty() const
	{
		return top == nullptr;
	}
};

int main()
{
	Stack stack;

	// Insertar elementos en la pila
	stack.push(10);
	stack.push(20);
	stack.push(30);

	// Mostrar los elementos de la pila
	while (!stack.isEmpty())
	{
		std::cout << "Elemento en el tope de la pila: " << stack.peek() << std::endl;
		stack.pop();
	}

	return 0;
}
