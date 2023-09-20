#include <iostream>
#include <array>

using namespace std;

const int TAM = 5;

typedef array<char, TAM> TArrayCHAR;

void escribir_array(TArrayCHAR minombre1, int estado)
{
    // Estado = 0 --> Invertido
    if (estado == 0)
    {
        for (int i = 4; i >= 0; i--)
        {
            cout << minombre1[i];
        }
    }
    // Estado = 1 --> Normal
    else if (estado == 1)
    {
        for (int i = 0; i < 5; i++)
        {
            cout << minombre1[i];
        }
    }
    else
    {
        cout << "Error, solo puedes introducir 0 y 1" << endl;
    }
    cout << endl;
}

int main()
{
    TArrayCHAR minombre1 = {'j', 'a', 'i', 'm', 'e'};
    TArrayCHAR minombre2 = {'j', 'e', 's', 'u', 's'};

    cout << "Palabra normal:" << endl;
    escribir_array(minombre1, 1);
    escribir_array(minombre2, 1);

    cout << "Palabra invertida:" << endl;
    escribir_array(minombre1, 0);
    escribir_array(minombre2, 0);

    return 0;
}