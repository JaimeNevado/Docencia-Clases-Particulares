#include <iostream>
#include <fstream>

int main()
{
	std::ifstream archivo;

	archivo.open("maikel.txt");

	char letra;

	if (!archivo)
	{
		std::cout << "El archivo no existe" << std::endl;
	}
	else
	{
		std::cout << "El archivo SI existe" << std::endl;
		int i = 0;
		int suma = 0;
		// End Of File (eof)
		archivo.get(letra);
		while (!archivo.eof())
		{
			// std::cout << letra;
			if (letra != '\n')
			{
				suma = suma + (letra - '0');
			}
			archivo.get(letra);

			i++;
		}

		std::cout << suma << std::endl;
	}

	char pal = 126;
	std::cout << pal << std::endl;

	return 0;
}