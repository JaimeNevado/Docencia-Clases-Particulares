/*
Ejercicio 1: Agregar elementos
Crea un vector de enteros, agrega algunos elementos usando push_back()
y luego imprime el contenido del vector.

*/

#include <iostream>
#include <vector>

int main()
{
	std::vector<int> vec;
	vec.push_back(10);
	vec.push_back(20);
	vec.push_back(30);

	std::cout << "Contenido del vector: ";
	for (int i = 0; i < vec.size(); i++)
	{
		std::cout << vec[i] << " ";
	}
	std::cout << std::endl;

	return 0;
}
