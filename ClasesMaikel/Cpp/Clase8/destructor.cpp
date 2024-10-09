#include <iostream>
#include <string>

class Persona
{
private:
	std::string nombre;

public:
	// Constructor
	Persona(const std::string &nombre) : nombre(nombre)
	{
		std::cout << "Se ha creado una persona llamada " << nombre << "." << std::endl;
	}

	// Destructor
	~Persona()
	{
		std::cout << "Se ha destruido a " << nombre << "." << std::endl;
	}

	std::string getNombre()
	{
		return nombre;
	}
};

int main()
{
	// Creamos objetos Persona directamente
	Persona persona1("Juan");
	Persona persona2("María");
	Persona persona3("Carlos");

	std::cout << persona1.getNombre() << std::endl;

	return 0;
}
