/*
Ejercicio 3: Tamaño y vacío
Verifica si el vector está vacío utilizando empty()
y, si no lo está, imprime su tamaño usando size().

*/

#include <iostream>
#include <vector>

int main()
{
	std::vector<int> vec = {10, 20, 30};

	if (!vec.empty())
	{
		std::cout << "El vector no está vacío." << std::endl;
		std::cout << "Tamaño del vector: " << vec.size() << std::endl;
	}
	else
	{
		std::cout << "El vector está vacío." << std::endl;
	}

	return 0;
}
