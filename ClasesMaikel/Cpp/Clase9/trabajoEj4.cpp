#include <iostream>
#include <string>

struct Estudiante
{
	std::string nombre;
	int edad;
};

int main()
{
	Estudiante *est = new Estudiante;

	// Asignar valores a la estructura
	est->nombre = "Juan Perez";
	est->edad = 20;

	// Mostrar la información del estudiante utilizando el puntero
	std::cout << "Nombre: " << est->nombre << std::endl;
	std::cout << "Edad: " << est->edad << std::endl;

	// Liberar la memoria asignada en el heap
	delete est;

	return 0;
}
