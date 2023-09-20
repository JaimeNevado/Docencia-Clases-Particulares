#include <iostream>

using namespace std;

bool esPrimo(int numero)
{
	if (numero <= 1)
	{
		return false; // Los números menores o iguales a 1 no son primos
	}

	for (int i = 2; i < numero; ++i)
	{
		if (numero % i == 0)
		{
			return false; // Si es divisible por algún número distinto de 1 y sí mismo, no es primo
		}
	}

	return true; // Si no fue divisible por ningún número, es primo
}

void lista_primos(int limite)
{
	cout << "Lista de primos menores que " << limite << endl;
	for (int i = 2; i <= limite; i++)
	{
		if (esPrimo(i))
		{
			cout << i << " ";
		}
	}
	cout << endl;
}

int main()
{
	int num;

	cout << "Ingrese el limite: ";
	cin >> num;

	lista_primos(num);

	return 0;
}
