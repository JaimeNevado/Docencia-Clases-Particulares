package clase1;

public class ejercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] nombres = {"Luis", "Samuel", "Sophia", "Jaime", "Sonia", "Santiago", "Sara"};

        // Utilizando un bucle for para recorrer la lista
        for (String nombre : nombres) {
            if (nombre.charAt(0) == 'S') {
                System.out.println(nombre);
            }
        }
	}

}
