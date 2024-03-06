#include <iostream>

using namespace std;

// Referencia (Original)
void pedirNombre(string &nombre)
{
	cout << "Dime tu nombre perro: " << endl;
	cin >> nombre;
}

// Parámetro (Copia)
void saludar(string nombre)
{
	cout << "Tu nombre de perro es: " << nombre << endl;
}

int main()
{
	string nombre;
	pedirNombre(nombre);

	cout << "Tu nombre de perro es: " << nombre << endl;
	return 0;
}