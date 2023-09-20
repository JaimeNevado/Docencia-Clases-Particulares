// Menú matrices

#include <iostream>
#include <array>

using namespace std;

const int TAM = 2;

typedef array<int, TAM> TFila;
typedef array<TFila, TAM> TMatriz;

void escribir_matriz(TMatriz matriz)
{
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			cout << matriz[i][j] << " ";
		}
		cout << endl;
	}
}

void sumar_matrices(TMatriz matrizA, TMatriz matrizB)
{
	TMatriz resultado;
	cout << "La matriz resultado de la suma es: " << endl;
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			resultado[i][j] = matrizA[i][j] + matrizB[i][j];
		}
	}
	escribir_matriz(resultado);
}

void restar_matrices(TMatriz matrizA, TMatriz matrizB)
{
	TMatriz resultado;
	cout << "La matriz resultado de la resta es: " << endl;
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			resultado[i][j] = matrizA[i][j] - matrizB[i][j];
		}
	}
	escribir_matriz(resultado);
}

void multiplicar_matrices(TMatriz matrizA, TMatriz matrizB)
{
	TMatriz resultado;
	cout << "La matriz resultado de la multiplicación es: " << endl;
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			resultado[i][j] = matrizA[i][j] * matrizB[i][j];
		}
	}
	escribir_matriz(resultado);
}

void dividir_matrices(TMatriz matrizA, TMatriz matrizB)
{
	TMatriz resultado;
	cout << "La matriz resultado de la división es: " << endl;
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			resultado[i][j] = matrizA[i][j] / matrizB[i][j];
		}
	}
	escribir_matriz(resultado);
}

void ingresar_matriz(TMatriz &matriz)
{
	for (int i = 0; i < TAM; i++)
	{
		for (int j = 0; j < TAM; j++)
		{
			cout << "Ingrese el numero en la posicion: " << i << "," << j << ":";
			cin >> matriz[i][j];
		}
	}
}

void menu(TMatriz &matrizA, TMatriz &matrizB)
{
	int opcion = 1;
	bool estado = false;
	while (opcion != 0)
	{
		cout << "------Menú de matrices------" << endl;
		cout << "1) Ingresar Matrices:" << endl;
		cout << "2) Sumar matrices:" << endl;
		cout << "3) Restar matrices:" << endl;
		cout << "4) Multiplicar matrices:" << endl;
		cout << "5) Dividir matrices:" << endl;
		cin >> opcion;
		if (opcion == 1)
		{
			cout << "Ingrese los valores a la matriz:" << endl;
			ingresar_matriz(matrizA);
			ingresar_matriz(matrizB);
			estado = true;
		}
		else if (estado)
		{
			if (opcion == 2)
			{
				sumar_matrices(matrizA, matrizB);
			}
			else if (opcion == 3)
			{
				restar_matrices(matrizA, matrizB);
			}
			else if (opcion == 4)
			{
				multiplicar_matrices(matrizA, matrizB);
			}
			else if (opcion == 5)
			{
				dividir_matrices(matrizA, matrizB);
			}
			else
			{
				cout << "Ha habido un error con los números introducidos" << endl;
			}
		}
		else if (opcion > 5 || opcion < 0)
		{
			cout << "Opción del menú inválida, seleccione otro número" << endl;
		}
		else if (estado == false)
		{
			cout << "Ingresa las matrices primero" << endl;
		}
	}
}
int main()
{
	TMatriz matrizA;
	TMatriz matrizB;
	menu(matrizA, matrizB);
}