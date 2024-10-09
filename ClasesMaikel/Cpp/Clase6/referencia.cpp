/*
Ejercicio 3: Tamaño y vacío
Verifica si el vector está vacío utilizando empty()
y, si no lo está, imprime su tamaño usando size().

*/

#include <iostream>
#include <vector>

void cambiarValor(int &c)
{
	c = 19;
}

int main()
{
	int valor = 10;
	std::cout << valor << std::endl;
	cambiarValor(valor);
	std::cout << valor << std::endl;

	return 0;
}
