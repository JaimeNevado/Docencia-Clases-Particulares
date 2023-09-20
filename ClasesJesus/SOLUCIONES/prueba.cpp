#include <iostream>
#include <array>
using namespace std;

const int TAM = 5;

typedef array<int, TAM> Tarrayint;
typedef array<Tarrayint, TAM> TMatrizInt;

void imprimir_matriz(TMatrizInt numeros)
{
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            cout << numeros[i][j];
        }
        cout << endl;
    }
}

void separar_matrices(TMatrizInt mat)
{
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            if (mat[i][j] % 2 == 0)
            {
                mat1[i][j]
            }
        }
    }
}

int main()
{
    TMatrizInt numeros = {{{1, 2, 3, 4, 5},
                           {3, 4, 5, 6, 7},
                           {3, 4, 5, 6, 7},
                           {3, 4, 5, 6, 7},
                           {3, 4, 5, 6, 7}}};

    return 0;
}