#include <iostream>
#include <string>

// Definición de un struct llamado Punto
struct Punto
{
	int x;
	int y;
};

int main()
{
	// Crear una instancia de Punto
	Punto punto1;

	// Asignar valores a los miembros del struct
	punto1.x = 5;
	punto1.y = 10;

	// Imprimir los valores de los miembros del struct
	std::cout << "Coordenadas del punto: (" << punto1.x << ", " << punto1.y << ")" << std::endl;

	return 0;
}
