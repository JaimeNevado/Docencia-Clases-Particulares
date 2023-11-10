package clase3;

public class ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int numeros[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		int base = 7;
		
		System.out.println("Esta es la tabla del " + base);
		for(int numero : numeros) {
			System.out.println(base*numero);
		}

	}

}
