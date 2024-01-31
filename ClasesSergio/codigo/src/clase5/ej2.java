package clase5;

public class ej2 {

    public static void main(String[] args) {
    	int[][] m = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 1, 1, 5},
                {4, 4, 5, 6}
            };
        
    	escribirMatrizTriangulo(m);
       
    }

    private static void escribirMatrizTriangulo(int[][] m) {
    	for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[i].length; j++) {
                if (i <= j) {
                    System.out.print(m[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

}
