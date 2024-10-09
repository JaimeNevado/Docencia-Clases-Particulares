package clase3;

public class ejercicio1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int ahorros[] = {2156, 5126, 1287, 2452, 4125};
		
		System.out.println("Las cuentas con más de 3000€ tienen: ");
		for (int cantidad : ahorros) {
			if (cantidad >= 3000) {
				System.out.println(cantidad + "€");
			}
		}
	}

}
