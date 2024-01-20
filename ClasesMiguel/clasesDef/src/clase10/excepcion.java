package clase10;

public class excepcion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			System.out.println(2/0);			
		} catch (ArithmeticException e) {
			System.out.println("Error al dividir entre 0");
		}
		
	}
	

}

