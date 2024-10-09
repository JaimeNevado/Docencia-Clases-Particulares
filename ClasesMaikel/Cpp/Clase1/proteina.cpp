#include <iostream>

using namespace std;

class Persona
{
private:
	string nombre;
	int edad;
	double altura;

public:
	Persona(string n, int e, double a)
	{
		nombre = n;
		edad = e;
		altura = a;
	}
	void saludar()
	{
		cout << "Hola!!" << endl;
	}

	// Getters
	int getEdad()
	{
		return edad;
	}

	string getNombre()
	{
		return nombre;
	}

	double getAltura()
	{
		return altura;
	}

	// Setters
	void setNombre(string n)
	{
		nombre = n;
	}
};

int main()
{
	Persona persona1("Jaime", 20, 1.8);
	Persona persona2("Manueh", 13, 4);

	cout << persona2.getNombre() << endl;

	persona2.setNombre("Maikel");

	cout << persona2.getNombre() << endl;

	return 0;
}