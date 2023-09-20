#include <iostream>
#include <array>

using namespace std;

const int TAM = 4;

typedef array<int, TAM> TArray;
typedef array<TArray, TAM> TMatriz;

void escribir(const TMatriz &m)
{

	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM - i; j++)
		{
			cout << m[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main()
{
	TMatriz matriz = {{
		{1, 2, 3, 4},
		{7, 8, 9, 7},
		{1, 4, 5, 3},
		{9, 2, 2, 1},
	}};

	escribir(matriz);

	return 0;
}
