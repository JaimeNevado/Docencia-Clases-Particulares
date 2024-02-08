package clase8;

public class ej3 {
	public static String decimalABinario(int numero) {
		if (numero == 0) {
			return "0";
		}

		boolean esNegativo = false;
		if (numero < 0) {
			esNegativo = true;
			numero = numero * -1;
		}

		String resultado = "";
		while (numero > 0) {
			int residuo = numero % 2;
			resultado = residuo + resultado;
			numero /= 2;
		}

		if (esNegativo) {
			resultado = "-" + resultado;
		}

		return resultado;
	}

	public static void main(String[] args) {
		int numeroPositivo = 42;
		int numeroNegativo = -42;

		System.out.println("El número " + numeroPositivo + " en binario es: " + decimalABinario(numeroPositivo));
		System.out.println("El número " + numeroNegativo + " en binario es: " + decimalABinario(numeroNegativo));
	}
}
