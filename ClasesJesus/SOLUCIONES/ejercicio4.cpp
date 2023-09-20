#include <iostream>
#include <array>
using namespace std;
float hacer_media(float suma, int cantidad)
{
	float media = suma / cantidad;

	return media;
}
int main()
{
	float suma = 0;
	int cantidad = 0;
	float nota;

	cout << "Dime las notas: ";
	cin >> nota;

	while (nota <= 10 && nota >= 0)
	{
		suma = suma + nota;
		cantidad++;
		cout << "Dime las notas :";
		cin >> nota;
	}

	cout << "La media final es " << hacer_media(suma, cantidad) << endl;

	return 0;
}
