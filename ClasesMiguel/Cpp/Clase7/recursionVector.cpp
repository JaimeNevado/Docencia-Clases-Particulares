#include <iostream>
#include <vector>

#include <vector>

void eliminarElementos(std::vector<int> &v)
{
	// Base case: si el vector está vacío, termina la recursión
	if (v.empty())
		return;

	// Elimina el último elemento del vector
	v.pop_back();

	// Llama a la función de nuevo con el vector actualizado
	eliminarElementos(v);
}

int main()
{
	std::vector<int> vect;

	vect.push_back(1);
	vect.push_back(2);
	vect.push_back(3);

	std::cout << "Vector original:" << std::endl;
	for (int numero : vect)
	{
		std::cout << numero << std::endl;
	}

	eliminarElementos(vect);

	std::cout << "\nVector despues de eliminar elementos:" << std::endl;
	for (int numero : vect)
	{
		std::cout << numero << std::endl;
	}

	return 0;
}
