package clase6;

public class ejercicio3 {

	public static double calcularNotaMedia(double[] notas) {
		double suma = 0;
		for (double elemento : notas) {
			suma += elemento;
		}
		return suma / notas.length;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double[] notas = {3, 4 ,2, 6, 3, 8, 10, 7};
		double media = calcularNotaMedia(notas);
		System.out.println("La nota media es: " + media);
	}

}
