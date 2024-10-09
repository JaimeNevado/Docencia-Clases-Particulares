#include <iostream>
#include <vector>

int escribirTexto(int n)
{
	// Caso base
	if (n == 1)
	{
		return n;
	}
	else
	{
		return n + suma(n - 1);
	}
}

int main()
{
	int n = 4;
	int solucion = suma(n);
	std::cout << "Solucion: " << solucion << std::endl;
	return 0;
}