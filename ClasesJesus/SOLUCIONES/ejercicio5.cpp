#include <iostream>
#include <array>
using namespace std;
const int TAM = 4;
typedef array<int, TAM> Tarrayint;

void escribir_array(Tarrayint array1)
{
	for (int i = 0; i < TAM; i++)
	{
		cout << array1[i];
	}
	cout << endl;
}

void pedir_datos(Tarrayint &array1)
{
	for (int i = 0; i < TAM; i++)
	{
		cout << "ingrese los datos: ";
		cin >> array1[i];
	}
}

Tarrayint invertir_array(Tarrayint array1)
{
	Tarrayint arrayCopia = array1;
	int j = TAM - 1;
	for (int i = 0; i < TAM; i++)
	{
		array1[i] = arrayCopia[j];
		j--;
	}
	return array1;
}

int main()
{

	Tarrayint array1;
	Tarrayint arrayinvertido;
	pedir_datos(array1);
	cout << "el array original es " << endl;
	escribir_array(array1);
	cout << "--------------------" << endl;
	cout << "el array invertido es" << endl;
	arrayinvertido = invertir_array(array1);
	escribir_array(arrayinvertido);
	return 0;
}
