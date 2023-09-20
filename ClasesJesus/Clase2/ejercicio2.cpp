#include <iostream>
#include <array>

using namespace std;

const int TAM = 6;

typedef array<int, TAM> TArray;

TArray sumar_array(TArray array1, TArray array2)
{
    TArray arrayResultado;
    for (int i = 0; i < TAM; i++)
    {
        arrayResultado[i] = array1[i] + array2[i];
    }
    return arrayResultado;
}

void escribir_array(TArray arrayPro)
{
    cout << "El array resultado es: " << endl;
    for (int i = 0; i < TAM; i++)
    {
        cout << arrayPro[i] << ", ";
    }
    cout << endl;
}

int main()
{
    TArray primerArray = {1, 2, 3, 4, 5, 6};
    TArray segundoArray = {3, 4, 2, 5, 7, 8};
    TArray resultado = sumar_array(primerArray, segundoArray);
    escribir_array(resultado);
    return 0;
}
