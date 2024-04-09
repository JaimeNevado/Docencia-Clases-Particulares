#include <iostream>

// Definición de una función plantilla
template <typename T>
T sumar(T a, T b)
{
	return a + b;
}

int main()
{
	// Ejemplo de uso de la función plantilla
	int resultado1 = sumar(5, 3);		 // Llama a sumar<int>(5, 3)
	double resultado2 = sumar(3.5, 2.5); // Llama a sumar<double>(3.5, 2.5)

	// Imprimir resultados
	std::cout << "Suma de enteros: " << resultado1 << std::endl;
	std::cout << "Suma de flotantes: " << resultado2 << std::endl;

	return 0;
}
