#include <iostream>
#include <array>

using namespace std;

const int TAM = 6;

typedef array<int, TAM> Tarray;
typedef array<Tarray, TAM> Tmatriz;

Tmatriz sumar_matrices(Tmatriz mat1, Tmatriz mat2)
{
    Tmatriz resultado;
    for (int i = 0; i < TAM; ++i)
    {
        for (int j = 0; j < TAM; ++j)
        {
            resultado[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
    return resultado;
}

void escribir_matriz(Tmatriz mat)
{
    for (int i = 0; i < TAM; ++i)
    {
        for (int j = 0; j < TAM; ++j)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    Tmatriz matriz1 = {{{1, 2, 3, 4, 5, 6},
                        {7, 8, 9, 10, 11, 12},
                        {13, 14, 15, 16, 17, 18},
                        {19, 20, 21, 22, 23, 24},
                        {25, 26, 27, 28, 29, 30},
                        {31, 32, 33, 34, 35, 36}}};

    Tmatriz matriz2 = {{{9, 8, 7, 6, 5, 4},
                        {3, 2, 1, 0, -1, -2},
                        {-3, -4, -5, -6, -7, -8},
                        {-9, -10, -11, -12, -13, -14},
                        {-15, -16, -17, -18, -19, -20},
                        {-21, -22, -23, -24, -25, -26}}};

    Tmatriz solucion = sumar_matrices(matriz1, matriz2);
    escribir_matriz(solucion);

    return 0;
}
