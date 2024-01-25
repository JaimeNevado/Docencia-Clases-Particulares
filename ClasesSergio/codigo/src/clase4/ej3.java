package clase4;

public class ej3 {

	public static void main(String[] args) {
		int[] cantidades = {1500, 2000, 3000, 2500, 1800, 3500, 4000, 2200, 2800, 3200, 2700, 1900, 2300, 2600};
		int maximo = 0;
		
		for (int numero : cantidades) {
			if (numero > maximo) {
				maximo = numero;
			}
		}
		
		System.out.println("La cuenta con más dinero tiene: " + maximo + "€");
	}

}
