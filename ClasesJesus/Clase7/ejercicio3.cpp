#include <iostream>
using namespace std;

bool esPrimo(int numero)
{

	bool estado = true;
	if (numero <= 1)
	{
		estado = false; // Los números menores o iguales a 1 no son primos
	}

	for (int i = 2; i < numero; ++i)
	{
		if (numero % i == 0)
		{
			estado = false; // Si es divisible por algún número distinto de 1 y sí mismo, no es primo
		}
	}

	return estado; // Si no fue divisible por ningún número, es primo
}

int main()
{

	int num;
	int mayor;
	cout << "Introduzca una secuencia de numeros enteros positivos (0 para terminar):";

	cin >> num;
	mayor = -1;
	while (num != 0)
	{
		if (esPrimo(num))
		{
			if (num > mayor)
			{
				mayor = num;
			}
		}
		cin >> num;
	}

	if (mayor == -1)
	{
		cout << "No hay ningun primo en la secuencia";
	}
	else
	{
		cout << "El mayor primo de la secuencia es: " << mayor;
	}
	return 0;
}