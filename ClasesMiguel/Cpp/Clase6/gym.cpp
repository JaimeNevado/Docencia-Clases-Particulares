#include <iostream>
#include <vector>
#include <string>

class Persona
{
private:
	std::string nombre;
	int edad;
	double peso;
	double pesoEnBanca;

public:
	Persona(const std::string &_nombre, int _edad, double _peso, double _pesoEnBanca)
		: nombre(_nombre), edad(_edad), peso(_peso), pesoEnBanca(_pesoEnBanca) {}

	// Getters y setters

	void mostrarDatos() const
	{
		std::cout << "Nombre: " << nombre << ", Edad: " << edad << ", Peso: " << peso << ", Peso en banca: " << pesoEnBanca << std::endl;
	}
};

void agregarPersona(std::vector<Persona> &personas)
{
	std::string nombre;
	int edad;
	double peso;
	double pesoEnBanca;

	std::cout << "Ingrese el nombre: ";
	std::cin >> nombre;
	std::cout << "Ingrese la edad: ";
	std::cin >> edad;
	std::cout << "Ingrese el peso: ";
	std::cin >> peso;
	std::cout << "Ingrese el peso en banca: ";
	std::cin >> pesoEnBanca;
	personas.push_back(Persona(nombre, edad, peso, pesoEnBanca));
}

void eliminarPersona(std::vector<Persona> &personas)
{
	if (!personas.empty())
	{
		personas.pop_back();
		std::cout << "Se ha eliminado la última persona del gimnasio." << std::endl;
	}
	else
	{
		std::cout << "No hay personas en el gimnasio para eliminar." << std::endl;
	}
}

void eliminarPersonas(std::vector<Persona> &personas)
{
	if (!personas.empty())
	{
		while (personas.size() != 0)
		{
			personas.pop_back();
		}
	}
}

bool gimnasioLleno(const std::vector<Persona> &personas, int capacidadMaxima)
{
	return personas.size() >= capacidadMaxima;
}

void mostrarPersonas(const std::vector<Persona> &personas)
{
	if (!personas.empty())
	{
		std::cout << "Personas en el gimnasio:" << std::endl;
		for (const Persona &p : personas)
		{
			p.mostrarDatos();
		}
	}
	else
	{
		std::cout << "No hay personas en el gimnasio." << std::endl;
	}
}

int main()
{
	std::vector<Persona> personas;
	int capacidadMaxima = 70; // Capacidad máxima del gimnasio

	// Agregar personas al gimnasio
	agregarPersona(personas);
	agregarPersona(personas);
	agregarPersona(personas);

	// Mostrar todas las personas en el gimnasio
	mostrarPersonas(personas);

	// Eliminar una persona del gimnasio
	eliminarPersonas(personas);

	mostrarPersonas(personas);

	// Verificar si el gimnasio está lleno
	if (gimnasioLleno(personas, capacidadMaxima))
	{
		std::cout << "El gimnasio está lleno." << std::endl;
	}
	else
	{
		std::cout << "El gimnasio no está lleno." << std::endl;
	}

	// (gimnasioLleno(personas, capacidadMaxima) ? "Sí" : "No")

	return 0;
}
