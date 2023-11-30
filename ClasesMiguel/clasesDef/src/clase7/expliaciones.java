package clase7;

public class expliaciones {

	public static void comprobar(int[] arr) {
		if (arr == null) {
			System.out.println("Error");
		} else if (arr.length == 0){
			System.out.println("Está vacío");
		} else {
			int tamaño = arr.length;
			System.out.println("Tiene " + tamaño + " elementos");			
		}

	}

	public static void main(String[] args) {
		int[] array = null;
		comprobar(array);
	}

}
