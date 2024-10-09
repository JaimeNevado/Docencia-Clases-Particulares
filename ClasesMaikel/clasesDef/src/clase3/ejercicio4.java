package clase3;

public class ejercicio4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String palabra = "azul";
		
		if (palabra.charAt(0) == palabra.charAt(palabra.length()-1)) {
			System.out.println(palabra+" SI es una palabra simétrica");
		} else {
			System.out.println(palabra+" NO es una palabra simétrica");			
		}
	}

}
