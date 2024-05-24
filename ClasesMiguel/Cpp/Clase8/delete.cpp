#include <iostream>

int main()
{
	// Asignamos memoria para un entero en el montón (heap)
	int numero = 5;
	int *ptr = &numero;

	// Imprimimos el valor del entero
	std::cout << "Valor antes de eliminar: " << *ptr << std::endl;

	// Liberamos la memoria utilizando delete
	delete ptr;

	// Intentamos acceder al valor después de eliminar
	// Esto podría causar un comportamiento indefinido ya que la memoria ya no está asignada
	std::cout << "Valor después de eliminar: " << *ptr << std::endl;

	return 0;
}
