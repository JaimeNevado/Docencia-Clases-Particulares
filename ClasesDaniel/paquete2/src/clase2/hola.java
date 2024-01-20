package clase2;

public class hola {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] carton = new int[9];

		carton[4] = -1;
		carton[2] = -1;
		carton[5] = -1;
		carton[7] = -1;

		imprimirArray(carton);

	}

	public static void imprimirArray(int[] a) {
		for (int i = 0; i < a.length; i++) {
			if (a[i] == -1) {
				System.out.print("  " );
			} else {
				System.out.print(a[i] );
			}
		}
	}

}
