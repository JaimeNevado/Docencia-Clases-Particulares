#include <iostream>
using namespace std;

float calcularCuadrado(float numero)
{
    float potencia = numero * numero;
    return potencia;
}

int main()
{
    float numeroUsuario;

    cout << "Ingrese un número: ";
    cin >> numeroUsuario;

    float cuadrado = calcularCuadrado(numeroUsuario);

    cout << "El cuadrado de " << numeroUsuario << " es: " << cuadrado << endl;

    return 0;
}
