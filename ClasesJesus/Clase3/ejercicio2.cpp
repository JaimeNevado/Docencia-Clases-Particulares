#include <iostream>
#include <array>
using namespace std;

const int TAM = 5;

typedef array<int, TAM> Tarray;

bool comprobar_palindromo(Tarray array1, Tarray array2)
{
    Tarray apoyo;
    int j = 0;
    bool estado = true;
    for (int i = TAM - 1; i >= 0; i--)
    {
        apoyo[j] = array1[i];
        j = j + 1;
    }
    for (int i = 0; i < TAM; i++)
    {
        if (apoyo[i] != array2[i])
        {
            estado = false;
        }
    }
    return estado;
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
    int i = 0;
    int resultado = 0;
    Tarray array1 = {1, 2, 3, 4, 5};
    Tarray array2 = {5, 4, 3, 2, 1};

    cout << "El array: ";
    escribir_array(array1);
    cout << "Y el array: ";
    escribir_array(array2);
    if (comprobar_palindromo(array1, array2))
    {
        cout << "Son palindromos" << endl;
    }
    else
    {
        cout << "No son es palindromos" << endl;
    }

    return 0;
}