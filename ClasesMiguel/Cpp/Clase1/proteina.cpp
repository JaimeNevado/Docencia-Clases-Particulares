#include <iostream>

using namespace std;

int sumar(int a, int b)
{
	int suma = a + b;
	return suma;
}

int main()
{
	int resultado = sumar(12, 3);

	cout << "El resultado es: " << resultado << endl;
	return 0;
}