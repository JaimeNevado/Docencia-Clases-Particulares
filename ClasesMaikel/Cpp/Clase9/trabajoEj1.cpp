#include <iostream>

int main()
{
    int var = 42;
    int *ptr = &var;

    std::cout << "Dirección de memoria de var: " << ptr << std::endl;

    return 0;
}
