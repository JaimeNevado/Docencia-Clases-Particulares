#include <iostream>
using namespace std;

bool esprimo(int numero)
{
	bool estado = true;
	if (numero <= 1)
	{
		estado = false;
	}
	else
	{
		for (int i = 2; i < numero; i++)
		{
			if (numero % i == 0)
			{
				estado = false;
			}
		}
	}
	return estado;
}
void lista_primos(int num)
{
	for (int i = 0; i < num; i++)
	{
		if (esprimo(i) == true)
		{
			cout << i << " ";
		}
	}
}

void pedir_numeros(int &num)
{
	cout << "Pedir secuencia de numeros: " << endl;
	cin >> num;
	int valormaximo = 0;
	while (num != 0)
	{
		if (esprimo(num) == true)
		{
			if (num > valormaximo)
			{
				valormaximo = num;
			}
		}
		cin >> num;
	}

	if (valormaximo == 0)
	{
		cout << "no hay ningun primo" << endl;
	}
	else
	{
		cout << "El numero primo mas grande es: " << valormaximo << endl;
	}
}
int main()
{
	int num;
	pedir_numeros(num);
	lista_primos(num);
	return 0;
}