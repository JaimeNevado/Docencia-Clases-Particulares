#include <iostream>
#include <array>

using namespace std;

const int TAM = 6;

typedef array<int, TAM> TArray;

void comparar_array(TArray array1, TArray array2)
{
    bool estado = true;
    for (int i = 0; i < TAM; i++)
    {
        if (array1[i] != array2[i])
        {
            estado = false;
        }
    }
    if (estado == false)
    {
        cout << "No son iguales" << endl;
    }
    else
    {
        cout << "Son iguales" << endl;
    }
}

int main()
{
    TArray minombre1 = {'j', 'a', 'i', 'm', 'e'};
    TArray minombre2 = {'j', 'e', 's', 'u', 's'};
    comparar_array(minombre1, minombre2);
    return 0;
}
