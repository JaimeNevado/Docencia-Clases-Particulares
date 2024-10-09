/*
Ejercicio 4: Acceso a elementos
Accede al primer y último elemento del vector utilizando front() y back(),
respectivamente, e imprímelos.
*/

#include <iostream>
#include <vector>

int main()
{
	std::vector<int> vec = {10, 20, 30};

	std::cout << "Primer elemento del vector: " << vec.front() << std::endl;
	std::cout << "Último elemento del vector: " << vec.back() << std::endl;

	return 0;
}
