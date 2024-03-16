package RepasoPracticaHerencia;

public class matrices {
	
	public static void printArray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			if (i == array.length - 1) {
				System.out.print(array[i]);
			} else {
				System.out.print(array[i] + ", ");				
			}
		}
		
		System.out.println();
	}

	public static void main(String[] args) {	
		
		int[][] matriz = {
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9}
		};

		int numero = matriz[0][0];
		// numero = 1
		
		
		
		
		
		

		printArray(ma
				
				
				trix[0]);
		printArray(matrix[1]);
		printArray(matrix[2]);
		
		System.out.println(matrix[1][1]);

	}

}
