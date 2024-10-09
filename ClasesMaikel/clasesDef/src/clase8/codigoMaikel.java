package clase8;

public class codigoMaikel {

    public static int[][] sumar_matrices (int[][] matriz1 , int[][] matriz2){
    	int filas = matriz1.length;

    	int columnas = matriz1[0].length;
    	
        int [][] resultado = new int [filas][columnas];


        for (int i = 0; i< resultado.length; i++) {
            for (int j = 0; j< resultado[0].length; j++ ) {
                resultado [i][j] = matriz1 [i][j] + matriz2 [i][j];

            }
        }
        return resultado;
    }
     public static void  imprimirResultado (int [][] resultado){
         for (int i = 0; i< resultado.length; i++) {
                for (int j = 0; j< resultado[0].length; j++ ) {
                    System.out.print(resultado [i][j] + " ");
                }
                System.out.println();
         } 
     }


    public static void main(String[] args) {
    	int m1[][] = {
    			{1, 2, 3, 10},
    			{1, 2, 3, 10},
    			{1, 2, 3, 10}
    	};
    	
    	int m2[][] = {
    			{1, 2, 3, 10},
    			{1, 2, 3, 10},
    			{1, 2, 3, 10}
    	};
    	
    	//System.out.println(matriz1.length);
    	
    	
        int[][] resultado = sumar_matrices(m1, m2);
        imprimirResultado(resultado);
    }

}