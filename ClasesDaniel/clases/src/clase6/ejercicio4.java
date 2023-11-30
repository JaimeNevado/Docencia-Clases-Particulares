package clase6;

public class ejercicio4 {

	public static int calcularMaximo(int a[]) {
		int maximo = a[0];
		for (int elemento : a) {
			if (elemento > maximo) {
				maximo = elemento;
			}
		}
		return maximo;
	}
	
	public static void main(String[] args) {
		int[] array = {1, 4, 5, 2, 4, 8, 2};
		int maximo = calcularMaximo(array);
		
		System.out.println("El numero máximo es: " + maximo);

	}

}
