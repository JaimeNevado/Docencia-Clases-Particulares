#include <iostream>

void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main()
{
	int var1 = 10;
	int var2 = 20;

	std::cout << "Antes del intercambio: var1 = " << var1 << ", var2 = " << var2 << std::endl;

	swap(&var1, &var2);

	std::cout << "Después del intercambio: var1 = " << var1 << ", var2 = " << var2 << std::endl;

	return 0;
}
