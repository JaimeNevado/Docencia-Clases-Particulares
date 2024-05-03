/*
Ejercicio 2: Eliminar elementos
Elimina el último elemento del vector usando pop_back()
y luego imprime el contenido actualizado del vector.

*/

#include <iostream>
#include <vector>

int main()
{
	// g++ -std=c++11 ej2.cpp
	std::vector<int> vec = {10, 20, 30};
	vec.pop_back();

	std::cout << "Contenido del vector después de eliminar el último elemento: ";
	for (int elem : vec)
	{
		std::cout << elem << " ";
	}
	std::cout << std::endl;

	return 0;
}
