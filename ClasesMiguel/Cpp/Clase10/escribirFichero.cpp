#include <iostream>
#include <fstream>

int main()
{
	std::ofstream archivo;

	archivo.open("maikel.txt");

	if (!archivo)
	{
		std::cout << "El archivo no existe" << std::endl;
	}
	else
	{
		std::cout << "El archivo SI existe" << std::endl;
		archivo << "Maikel está mazao" << std::endl;
	}

	return 0;
}