package clase5;

public class ejercicio5 {
	
	static void escribirArray(int[] array) {
		System.out.print("Elementos del array: ");

		// Imprimir cada elemento del array
		for (int elemento : array) {
			System.out.print(elemento + " ");
		}

		System.out.println(); // Imprimir nueva línea al final
	}
	
	static void cortarArray(int[] arrayOriginal, int N) {
		// Verificar si el arrayOriginal es nulo o vacío
		if (arrayOriginal == null || arrayOriginal.length == 0 || N <= 0) {
			System.out.println("El array original es nulo, vacío o N no es válido.");
			return;
		}

		// Verificar si N es mayor que la longitud del arrayOriginal
		if (N > arrayOriginal.length) {
			System.out.println("N es mayor que la longitud del array original.");
			System.out.println("Array cortado: ");
			escribirArray(arrayOriginal);
			return;
		}

		// Crear el arrayCortado con tamaño N
		int[] arrayCortado = new int[N];

		// Copiar los primeros N elementos desde arrayOriginal a arrayCortado
		for (int i = 0; i < N; i++) {
			arrayCortado[i] = arrayOriginal[i];
		}

		// Imprimir el arrayCortado
		System.out.println("Array cortado: ");
		escribirArray(arrayCortado);
	}

	public static void main(String[] args) {
		// Ejemplo de uso de la función
		int[] arrayOriginal = {2, 3, 5, 7, 7, 7 };
		int N = 3;

		// Llamada a la función para cortar el array
		cortarArray(arrayOriginal, N);
	}
}
