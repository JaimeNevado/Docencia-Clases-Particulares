#include <iostream>
#include <array>

using namespace std;

const int TAM = 7;

typedef array<int, TAM> TFila;
typedef array<TFila, TAM> TMatriz;

// inicializa a 1 la primera fila y la primera columna
void inicializar(TMatriz &m)
{

	for (int cont = 0; cont < TAM; cont++)
	{
		m[0][cont] = 1;
		m[cont][0] = 1;
	}
}

// construye la matriz con el triangulo de Pascal
void construir(TMatriz &m)
{

	inicializar(m);
	for (int i = 1; i < TAM - 1; i++)
	{
		for (int j = 1; j < TAM - 1; j++)
		{
			m[i][j] = m[i][j - 1] + m[i - 1][j];
		}
	}
}

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
	TMatriz pascal;

	construir(pascal);
	escribir(pascal);

	return 0;
}
