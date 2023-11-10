package clase0;

public class ejercicio2 {

	public static void main(String[] args) {
        double nota = 7.8;

        if (nota >= 9) {
            System.out.println("Sobresaliente");
        } else if (nota >= 7 && nota < 9) {
            System.out.println("Notable");
        } else if (nota >= 6 && nota < 7) {
            System.out.println("Bien");
        } else if (nota >= 5 && nota < 6) {
            System.out.println("Suficiente");
        } else {
            System.out.println("Insuficiente");
        }
	
	}

}
