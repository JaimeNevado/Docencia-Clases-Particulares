package clase8;

public class explicaciones {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        String[] nombres = {"Juan", "María", "Pedro", "Ana", "Carlos"};
        int[] valores = {4, 5, 5 ,10, 8};
        for (String nombre : nombres) {
        	System.out.printf("%-15s", nombre);
        }
        System.out.println();
        for (int i = 0; i < 5; i++) {
        	System.out.printf("%-15d", valores[i]);
        }
	}

}
