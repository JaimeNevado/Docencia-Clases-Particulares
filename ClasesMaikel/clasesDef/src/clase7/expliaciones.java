package clase7;

public class expliaciones {
	
	public static boolean esPar(int num) {
		boolean numeroPar = false;
		if (num % 2 == 0) {
			numeroPar = true;
		}
		return numeroPar;
	}
	
	public static void main(String[] args) {
		if (esPar(15)) {
			System.out.println("Es par");
		} else {
			System.out.println("No es par");
		}
	}

}
