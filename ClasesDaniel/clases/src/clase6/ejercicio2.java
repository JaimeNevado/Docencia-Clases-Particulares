package clase6;

public class ejercicio2 {
	
	public static double cuadrado(double radio) {
		return radio * radio;
	}
	
	public static void error() {
		System.out.println("Error");
	}
	
	public static double calcular_area_circulo(double radio) {
		double area = -1;
		if (radio <= 0) {
			error();
		} else {
			area = 3.14 * cuadrado(radio);			
		}
		return area;

	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double radio = 3;
		double area = calcular_area_circulo(radio);
		System.out.println("El area es: " + area);
	}

}
