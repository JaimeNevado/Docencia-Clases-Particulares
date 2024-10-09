#include <iostream>

using namespace std;

int main()
{
	int *punteroEntero;	   // Puntero a un entero
	double *punteroDouble; // Puntero a un número de punto flotante

	int num = 0;
	punteroEntero = &num;

	cout << "El numero es " << *punteroEntero << endl;
	return 0;
}