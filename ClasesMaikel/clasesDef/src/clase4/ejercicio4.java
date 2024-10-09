package clase4;

public class ejercicio4 {

	public static void main(String[] args) {
		int tamaño = 3;
		for (int i = 0; i< tamaño; i++) {
			for(int j = 0; j < tamaño; j++) {
				if (i >= j) {
					System.out.print("* ");			
				}
			}
			System.out.println();
		}
	}

}
