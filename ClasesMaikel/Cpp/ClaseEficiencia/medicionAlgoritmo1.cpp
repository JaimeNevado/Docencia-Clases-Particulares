#include <iostream>

// Función que suma dos números
int escribirNumeros(int tam)
{
	int numIteraciones = 0;
	while (numIteraciones < tam)
	{
		std::cout << ("Hola") << std::endl;
		numIteraciones++;
	}
	return numIteraciones;
}

int main()
{
	int resultado = escribirNumeros(10);
	std::cout << "El algoritmo tarda: " << resultado << std::endl;
	return 0;
}
