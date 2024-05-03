/*
Ejercicio 6: Redimensionamiento
Utiliza resize() para aumentar el tamaño del vector
y luego imprime su contenido.
*/

#include <iostream>
#include <vector>

int main()
{
	std::vector<int> vec = {10, 20, 30};

	vec.resize(5, 25); // Aumentar el tamaño del vector a 5 y rellenar con el valor 25

	std::cout << "Contenido del vector después del redimensionamiento: ";
	for (int elem : vec)
	{
		std::cout << elem << " ";
	}
	std::cout << std::endl;

	return 0;
}
