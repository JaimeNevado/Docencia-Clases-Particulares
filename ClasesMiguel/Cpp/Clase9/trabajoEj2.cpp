#include <iostream>

int main()
{
	int arr[5] = {1, 2, 3, 4, 5};
	int *ptr = arr;

	for (int i = 0; i < 5; ++i)
	{
		std::cout << "Dirección de memoria de arr[" << i << "]: " << (ptr + i) << std::endl;
	}

	return 0;
}
