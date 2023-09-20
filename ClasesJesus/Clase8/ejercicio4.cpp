#include <iostream>
#include <array>

using namespace std;

const int MAX = 3;
typedef array<int, MAX> TArray;

bool numeroCorrecto(int num)
{
	bool estado = false;
	if (num >= 0 && num <= 10)
	{
		estado = true;
	}
	return estado;
}

int main()
{
	int num = 0;
	int suma = 0;
	int contador = 0;
	float media = 0;

	cout << "Ingrese las notas de los alumnos:" << endl;
	cin >> num;

	while (numeroCorrecto(num))
	{
		suma = suma + num;
		contador++;
		cin >> num;
	}

	media = suma / contador;

	if (media >= 5)
	{
		cout << "Tu media es " << media << " y estás aprobado" << endl;
	}
	else
	{
		cout << "Tu media es " << media << " y estás suspenso" << endl;
	}

	return 0;
}
