#include <iostream>
#include <string>

struct Estudiante
{
	std::string nombre;
	int edad;
};

int main()
{
	Estudiante *e1;

	e1->edad = 19;
	e1->nombre = "Javieeeer";

	std::cout << e1->edad << std::endl;
	std::cout << e1->nombre << std::endl;

	return 0;
}