// Diseña un algoritmo que lea de teclado una secuencia de números entre 0 y 9 y cuente el
// número de veces que se repite cada dígito. La secuencia de números de entrada se da por
// finalizada al leer un número negativo y a priori no se puede determinar cuántos números
// contiene. Ejemplo de ejecución:

// Introduzca una secuencia de digitos (negativo termina):
// 1 8 7 3 4 8 5 9 5 0 0 4 8 4 5 3 2 8 -1
// La frecuencia de cada digito es:
// 0: 2
// 1: 1
// 2: 1
// 3: 2
// 4: 3
// 5: 3
// 6: 0
// 7: 1
// 8: 4
// 9: 1

#include <iostream>
#include <array>
using namespace std;
const int TAM = 10;

typedef array<int, TAM> TArray;

void inicializar(TArray &frec)
{
	for (int i = 0; i < TAM; i++)
	{
		frec[i] = 0;
	}
}
void calcular(TArray &frec)
{
	int dig;
	inicializar(frec);
	cout << "Introduzca una secuencia de digitos (negativo termina):\n";
	cin >> dig;
	while (dig >= 0)
	{
		if ((0 <= dig) && (dig <= 9))
		{
			frec[dig]++;
		}
		cin >> dig;
	}
}
void imprimir(const TArray &frec)
{
	cout << "La frecuencia de cada digito es:" << endl;
	for (int i = 0; i < TAM; i++)
	{
		cout << i << ": " << frec[i] << endl;
	}
}
int main()
{
	TArray frec;
	calcular(frec);
	imprimir(frec);
	return 0;
}