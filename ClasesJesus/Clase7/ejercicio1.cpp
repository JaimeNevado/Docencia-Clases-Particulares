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

int main()
{
	int num;

	cout << "Ingrese un número: ";
	cin >> num;

	if (esPrimo(num))
	{
		cout << num << " ES un número primo." << endl;
	}
	else
	{
		cout << num << " NO es un número primo." << endl;
	}

	return 0;
}
