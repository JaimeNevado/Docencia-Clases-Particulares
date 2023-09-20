#include <iostream>
using namespace std;

int sumarNumeros(int a, int b)
{
    return a + b;
}

int main()
{
    int num1, num2;

    cout << "Ingrese el primer número: ";
    cin >> num1;

    cout << "Ingrese el segundo número: ";
    cin >> num2;

    int suma = sumarNumeros(num1, num2);
    cout << "La suma es: " << suma << endl;

    return 0;
}
