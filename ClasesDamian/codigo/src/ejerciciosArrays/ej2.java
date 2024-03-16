package ejerciciosArrays;

public class ej2 {
	public static void main(String[] args) {
		String[] nombres = { "Luis", "Samuel", "Sophia", "Jaime", "Sonia", "Santiago", "Sara" };

		System.out.println("Nombres que empiezan con la letra 'S':");
		for (int i = 0; i < nombres.length; i++) {
			if (nombres[i].charAt(0) == 'S') {
				System.out.println(nombres[i]);
			}
		}
	}
}
