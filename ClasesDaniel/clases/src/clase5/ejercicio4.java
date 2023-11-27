package clase5;

public class ejercicio4 {
	// Función para escribir los elementos de un array
	static void escribirArray(int[] array) {
		System.out.print("Elementos del array: ");

		// Imprimir cada elemento del array
		for (int elemento : array) {
			System.out.print(elemento + " ");
		}

		System.out.println(); // Imprimir nueva línea al final
	}

	public static void main(String[] args) {
		// Crear un array de ejemplo
		int[] numeros = { 1, 3, 5, 7, 9 };

		// Llamada a la función para escribir el array
		escribirArray(numeros);
	}
}
