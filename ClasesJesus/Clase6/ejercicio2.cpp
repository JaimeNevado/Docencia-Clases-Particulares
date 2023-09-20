#include <iostream>
#include <array>

using namespace std;

const int TAM = 10;

typedef array<int, TAM> TArray;

int mayorLongitud(TArray &a)
{
	int mayor = 0;
	int longitud = 1;

	for (int i = 1; i < TAM; i++)
	{
		if (a[i - 1] > a[i])
		{
			if (longitud > mayor)
			{
				mayor = longitud;
			}
			longitud = 0;
		}
		longitud++;
	}
	if (longitud > mayor)
	{
		mayor = longitud;
	}

	return mayor;
}

void leer(TArray &a)
{

	cout << "Introduzca " << TAM << " numeros enteros: ";
	for (int i = 0; i < TAM; i++)
	{
		cin >> a[i];
	}
}

int main()
{
	TArray array;

	leer(array);

	cout << "La longitud de la mayor sub-sucesion es: " << mayorLongitud(array) << endl;

	return 0;
}
