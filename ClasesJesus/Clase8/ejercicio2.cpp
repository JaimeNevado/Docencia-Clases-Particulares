#include <iostream>
#include <array>
using namespace std;

const int TAM = 10; // Tamaño del array
typedef array<int, TAM> TArray;

int maximo(int a, int b)
{
	int valor = b;
	if (a > b)
	{
		valor = a;
	}
	return valor;
}

int mayorLongitud(TArray arr)
{
	int max_longitud = 0;	 // Almacena la longitud máxima de la sub-sucesión ordenada encontrada
	int longitud_actual = 1; // Almacena la longitud actual de la sub-sucesión ordenada

	// El ciclo recorre el array desde el segundo elemento (índice 1) hasta el último
	for (int i = 1; i < TAM; i++)
	{
		// Comparamos el elemento actual con el elemento anterior
		if (arr[i] >= arr[i - 1])
		{
			longitud_actual++; // Incrementamos la longitud actual si el elemento actual es mayor o igual al anterior
		}
		else
		{
			// Si el elemento actual es menor que el anterior, significa que la sub-sucesión ordenada actual se rompe
			max_longitud = maximo(max_longitud, longitud_actual); // Actualizamos la longitud máxima si es necesario
			longitud_actual = 1;								  // Reiniciamos la longitud actual a 1, ya que se rompió la sub-sucesión ordenada
		}
	}

	// Al final del ciclo, actualizamos la longitud máxima si es necesario (para el último segmento ordenado)
	return maximo(max_longitud, longitud_actual);
}

int main()
{
	TArray arr;

	for (int i = 0; i < TAM; i++)
	{
		cout << "Ingrese un número: ";
		cin >> arr[i];
	}

	cout << "La longitud de la mayor sub-sucesión ordenada es: " << mayorLongitud(arr) << endl;

	return 0;
}
