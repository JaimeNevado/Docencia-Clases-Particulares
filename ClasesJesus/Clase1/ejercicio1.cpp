#include <iostream>
using namespace std;

int main()
{
    float temperatura;

    cout << "Ingrese una temperatura en grados Celsius: ";
    cin >> temperatura;

    if (temperatura >= 30)
    {
        cout << "¡Hace calor!" << endl;
    }
    else if (temperatura <= 10)
    {
        cout << "¡Hace frío!" << endl;
    }
    else
    {
        cout << "La temperatura está bien" << endl;
    }

    return 0;
}
