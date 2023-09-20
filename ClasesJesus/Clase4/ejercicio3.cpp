#include <iostream>
#include <array>

using namespace std;

const int TAM = 3;

typedef array<int, TAM> Tarray;
typedef array<Tarray, TAM> Tmatriz;

Tmatriz construir_matriz_cruz()
{
	Tmatriz resultado;
	int centro = TAM / 2;

	for (int i = 0; i < TAM; ++i)
	{
		for (int j = 0; j < TAM; j++)
		{
			if (i == centro || j == centro)
			{
				resultado[i][centro] = 1;
				resultado[centro][i] = 1;
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
	Tmatriz solucion = construir_matriz_cruz();
	escribir_matriz(solucion);

	return 0;
}
