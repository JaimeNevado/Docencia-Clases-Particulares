

#include <iostream>
#include <string>
#include <array>

using namespace std;

const int MAX_PAL_DIST = 20;

typedef array<string, MAX_PAL_DIST> TArray;

void escribir(TArray a)
{
	cout << "Las palabras son:\n\n";
	for (int i = 0; i < MAX_PAL_DIST; i++)
	{
		cout << a[i] << " ";
	}
}

bool comprobar(TArray array, string pal)
{
	bool estado = false;
	for (int i = 0; i < array.size(); i++)
	{
		if (array[i] == pal)
		{
			cout << "La palabra ya existe" << endl;
			estado = true;
		}
	}
	return estado;
}

int main()
{
	int i = 0;
	TArray pal;

	cout << "Introduzca el texto (FIN para terminar):\n";

	cin >> pal[i];

	while (pal[i] != "FIN" || comprobar(pal, pal[i]))
	{
		i++;
		cin >> pal[i];
	}

	escribir(pal);

	return 0;
}
