/*
Ejercicio 5: Insertar y eliminar en posiciones específicas
Inserta un elemento en la posición 2 del vector utilizando insert() y
luego elimina el elemento en la posición 1 utilizando erase().
*/

#include <iostream>
#include <vector>

int main()
{
	std::vector<int> vec = {10, 20, 30};

	// Insertar elemento en la posición 2
	vec.insert(vec.begin() + 1, 15);

	// Eliminar elemento en la posición 1
	vec.erase(vec.begin());

	std::cout << "Contenido del vector después de insertar y eliminar: ";
	for (int elem : vec)
	{
		std::cout << elem << " ";
	}
	std::cout << std::endl;

	return 0;
}
