#include <iostream>
#include <array>
using namespace std;

const int TAM = 5;

typedef array<int, TAM> Tarray;

int valor_maximo(Tarray array1)
{
    int max = -99999;
    for (int i = 0; i < TAM; i++)
    {
        if (array1[i] >= max)
        {
            max = array1[i];
        }
    }
    return max;
}

void escribir_array(Tarray lol)
{
    for (int i = 0; i < TAM; i++)
    {
        cout << lol[i];
    }
    cout << endl;
}

int main()
{
    Tarray array1 = {1, 2, 3, 4, 5};

    cout << "El valor máximo es: " << valor_maximo(array1) << endl;

    return 0;
}