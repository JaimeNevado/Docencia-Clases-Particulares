#include <iostream>
#include <string>
#include <list>

using namespace std;

class Bench
{
private:
    int accesorios;
    int variantes;

public:
    Bench()
    {
        int v = variantes;
        int a = accesorios;
    }

    void mostrarVariantes()
    {
        cout << "Estas son las variantes de Banca :" << endl;
        cout << "1.Tempo / 2.Pausa / 3.Pines / 4.Grips / 5.Board / 6.Feets / 7.Bandas" << endl;
        cout << "selecciona la variante que quieres : " << endl;
    }

    string añadirVariante(string)
    {
        mostrarVariantes();
        int variante1;
        cin >> variante1;
        variante1 = variante1 - 1;

        list<string> miLista;
        miLista.push_back("Tempo");
        miLista.push_back("Pausa");
        miLista.push_back("Pines");
        miLista.push_back("Grips");
        miLista.push_back("Board");
        miLista.push_back("Feets");
        miLista.push_back("Bandas");

        for (string var : miLista)
        {
            if (var == variante1)
            {
            }
        }

        cout << "las variantes escogidas son " << *it << endl;

        cout << "deseas escoger mas variantes ? " << endl;
        cout << "1.SI " << endl;
        cout << "2.NO" << endl;
        int opcion1 = 0;
        cin >> opcion1;
        if (opcion1 == 1)
        {
            añadirVariante();
        }
        else if (opcion1 == 2)
        {
            return 0;
        }
        else
        {
            cout << "onde vas matao " << endl;
        }

        return variantes;
    }
};

int main()
{
    int seleccion = 0;
    cout << "Que ejercicio quieres seleccionar : " << endl;
    cout << "1. Squat " << endl;
    cout << "2. Bench " << endl;
    cout << "3. Deadlift " << endl;
    cin >> seleccion;

    if (seleccion == 1)
    {
        cout << "Hacemos el Squat loco" << endl;
    }
    else if (seleccion == 2)
    {
        int seleccion2 = 0;
        cout << "seleccione una de las dos opciones que quiera : " << endl;
        cout << "1. variantes " << endl;
        cout << "2. accesorios " << endl;
        cin >> seleccion2;

        if (seleccion2 == 1)
        {
            string variantesseleccionadas;
            Bench banca1;
            variantesseleccionadas = banca1.añadirVariante();
        }
        else if (seleccion2 == 2)
        {
        }
        else
        {
            cout << "Error colega" << endl;
        }
    }
    else if (seleccion == 3)
    {
        cout << "Hacemos el Deadlift loco" << endl;
    }
    else
    {
        cout << " la opcion elegida no es correcta " << endl;
    }
}