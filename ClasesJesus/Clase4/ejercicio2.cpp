#include <iostream>
#include <array>

using namespace std;

const int TAM = 3;

typedef array<int, TAM> Tarray;
typedef array<Tarray, TAM> Tmatriz;

Tmatriz construir_matriz_identidad()
{
	Tmatriz resultado;
	for (int i = 0; i < TAM; ++i)
	{
		for (int j = 0; j < TAM; ++j)
		{
			if (i == j)
			{
				resultado[i][j] = 1;
			}
			else
			{
				resultado[i][j] = 0;
			}
		}
	}
	return resultado;
}

void escribir_matriz(Tmatriz mat)
{
	for (int i = 0; i < TAM; ++i)
	{
		for (int j = 0; j < TAM; ++j)
		{
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
}

int main()
{
	Tmatriz solucion = construir_matriz_identidad();
	escribir_matriz(solucion);

	return 0;
}
