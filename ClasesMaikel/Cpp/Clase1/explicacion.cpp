#include <iostream>

using namespace std;

class Persona
{
private:
	string nombre;
	int edad;

public:
	Persona(string n, int e)
	{
		nombre = n;
		edad = e;
	}
	void saludar(string saludo)
	{
		cout << saludo << " soy " << nombre << endl;
		cout << "Tengo " << edad << " años" << endl;
	}

	string getNombre()
	{
		return nombre;
	}
};

int main()
{
	Persona persona1("Jaime", 20);

	cout << persona1.getNombre() << endl;
	return 0;
}