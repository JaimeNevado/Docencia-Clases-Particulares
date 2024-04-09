#include <iostream>

using namespace std;

class Persona
{
	// atributos
private:
	int edad;
	double altura;
	string nombre;

public:
	// Contructor
	Persona(int e, double a, string n) : edad(e), altura(a), nombre(n) {}

	void saludar()
	{
		cout << "Hola soy " << nombre << endl;
	}

	// getter
	string illoDameElNombre()
	{
		return nombre;
	}

	void cambiarNombre(string nuevoNombre)
	{
		nombre = nuevoNombre;
	}
};

int main()
{
	Persona p1(19, 1.80, "Maikel");

	cout << p1.illoDameElNombre() << endl;

	p1.cambiarNombre("Jaime");

	cout << p1.illoDameElNombre() << endl;

	return 0;
}