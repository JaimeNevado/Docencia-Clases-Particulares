#include <iostream>
#include <array>
#include <string>

using namespace std;

const int TAM = 2;

typedef array<string, TAM> Tarray;
typedef array<int, TAM> Tarrayint;

void escribir(Tarray array)
{
    for (int i = 0; i < TAM; i++)
    {
        cout << array[i] << endl;
    }
    cout << endl;
}

int main()
{
    string nombre = "Jesus";
    cout << nombre.size() << endl;
    return 0;
}
