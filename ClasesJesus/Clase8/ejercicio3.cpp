#include <iostream>
#include <array>

using namespace std;

const int MAX = 3;
typedef array<int, MAX> TArray;

bool buscarNumeroEnArray(const TArray &array, int num)
{
	bool encontrado = false;
	for (int i = 0; i < MAX; ++i)
	{
		if (array[i] == num)
		{
			encontrado = true;
		}
	}
	return encontrado;
}

int main()
{
	TArray array;

	cout << "Ingrese los elementos del array:" << endl;
	for (int i = 0; i < MAX; ++i)
	{
		cout << "Elemento " << i + 1 << ": ";
		cin >> array[i];
	}

	int num;
	cout << "Ingrese el número a buscar: ";
	cin >> num;

	if (buscarNumeroEnArray(array, num))
	{
		cout << "El número: " << num << " está en el array." << endl;
	}
	else
	{
		cout << "El número: " << num << " no está en el array." << endl;
	}

	return 0;
}
