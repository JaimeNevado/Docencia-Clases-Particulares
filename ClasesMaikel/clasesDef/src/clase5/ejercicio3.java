package clase5;

public class ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
            	if (i == j) {
            		System.out.print("X");         		
            	} else {
            		System.out.print("0");
            	}
            }
            System.out.println();
        }
	}

}
