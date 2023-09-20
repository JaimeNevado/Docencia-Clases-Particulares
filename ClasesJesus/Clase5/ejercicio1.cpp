#include <iostream>
#include <array>
using namespace std;

const int TAM = 3;

typedef array<int, TAM> TFila;
typedef array<TFila, TAM> TMatriz;

void rotar1vez(TMatriz &m)
{
	TMatriz maux;

	for (int fi = 0; fi < TAM; fi++)
	{
		for (int co = 0; co < TAM; co++)
		{
			maux[co][TAM - 1 - fi] = m[fi][co];
		}
	}

	m = maux;
}

void rotar(TMatriz &mat, int n)
{
	for (int i = 1; i <= n; i++)
	{
		rotar1vez(mat);
	}
}

void leer(TMatriz &m)
{

	for (int fi = 0; fi < TAM; fi++)
	{
		for (int co = 0; co < TAM; co++)
		{
			cin >> m[fi][co];
		}
	}
}

void escribir(const TMatriz &m)
{

	for (int fi = 0; fi < TAM; fi++)
	{
		for (int co = 0; co < TAM; co++)
		{
			cout << m[fi][co] << " ";
		}
		cout << endl;
	}
}

int main()
{
	TMatriz mat;
	int n;

	cout << "Introduzca los elementos de la matriz ("
		 << TAM << " x " << TAM << ") fila a fila:" << endl;
	leer(mat);

	cout << "\nIntroduzca el numero de rotaciones a realizar: ";
	cin >> n;

	rotar(mat, n);

	cout << "\nLa matriz resultado tras las rotaciones es:\n";
	escribir(mat);

	return 0;
}
