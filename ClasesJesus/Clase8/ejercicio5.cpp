#include <iostream>
#include <array>

using namespace std;

const int MAX = 4; // Tamaño máximo del array

typedef array<int, MAX> TArray;

void escribirArray(TArray array)
{
	for (int i = 0; i < MAX; ++i)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}

void invertirArray1(TArray &array)
{
	for (int i = 0; i < MAX / 2; ++i)
	{
		int temp = array[i];
		array[i] = array[MAX - 1 - i];
		array[MAX - 1 - i] = temp;
	}
}

void invertirArray2(TArray &array)
{
	int j = MAX;
	TArray array_extra = array;
	for (int i = 0; i < MAX; ++i)
	{
		array[j - 1] = array_extra[i];
		j--;
	}
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

	cout << "El array original es: " << endl;
	escribirArray(array);

	// invertirArray1(array);
	invertirArray2(array);

	cout << "Array invertido:" << endl;
	escribirArray(array);

	return 0;
}
