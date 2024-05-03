#include <iostream>
#include <vector>

void escribirVector(const std::vector<int> &v)
{
	for (int numero : v)
	{
		std::cout << numero << std::endl;
	}
}

int main()
{

	std::vector<int> vect;

	// Añadir elementos
	vect.push_back(8);	 // pos -> 0
	vect.push_back(10);	 // pos -> 1
	vect.push_back(888); // pos -> 2

	// Sacar tamaño de un vector
	int tamaño = vect.size();

	// Insertar el 33 en la primera posicion
	vect.insert(vect.begin(), 33);

	// Borrar un elemento en la primera posicion
	vect.erase(vect.begin());

	// Eliminar el último elemento
	vect.pop_back();

	// Borrar todos los elementos del vector
	vect.clear();

	escribirVector(vect);

	return 0;
}
