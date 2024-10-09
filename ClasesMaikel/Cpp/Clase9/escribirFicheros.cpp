#include <iostream>
#include <fstream>

int main()
{
	std::ofstream archivo;		// Declaramos el archivo de salida
	archivo.open("salida.txt"); // Abrimos el archivo "numeros.txt" en modo escritura

	if (!archivo)
	{ // Verificamos si se pudo abrir el archivo correctamente
		std::cout << "Error creando archivo";
	}
	else
	{
		for (int i = 0; i < 10; i++)
		{
			archivo << i << std::endl; // Escribimos los números del 0 al 9, uno por línea, en el archivo
		}
	}

	// El archivo se cierra automáticamente al salir del ámbito de la variable "archivo"
	return 0;
}
