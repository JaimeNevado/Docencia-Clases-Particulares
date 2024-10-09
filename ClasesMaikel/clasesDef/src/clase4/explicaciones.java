package clase4;

public class explicaciones {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array1 = {1, 2, 3, 4, 5, 6};
        int[] array2 = {3, 4, 2, 5, 7, 8};
        int[] arrayResultado = {0, 0, 0, 0, 0, 0};
        
       
        for (int i = 0; i < 6; i++) {
        	arrayResultado[i] = array1[i] + array2[i];
        }
        
        for (int num : arrayResultado) {
        	System.out.print(num + ", ");
        }
        
	}

}
