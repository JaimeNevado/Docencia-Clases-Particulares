#include <iostream>

// Función que suma dos números
int sumar(int a, int b)
{
	return a + b;
}

int main()
{
	int num1 = 3;
	int num2 = 4;
	int resultado = sumar(num1, num2);
	std::cout << "La suma de " << num1 << " y " << num2 << " es: " << resultado << std::endl;
	return 0;
}
