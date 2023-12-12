package clase8;

public class Ejercicio8 {
    public static void main(String[] args) {
        final int NUMERO_MESES = 12;

        int[] temperaturas = cargaTemperaturas(NUMERO_MESES);
        calculaImprimeMedia(temperaturas);
        pintaGrafica(temperaturas);
    }

    public static int[] cargaTemperaturas(int numeroMeses) {
        int[] temperaturas = new int[numeroMeses];
        temperaturas = generaAleatorio(temperaturas);
        return temperaturas;
    }

    public static int[] generaAleatorio(int t[]) {
    	t[0] = ((int) Math.floor(Math.random() * 45)) + 0;
    	for (int i = 1; i < t.length; i++) {
    		t[i] = ((int) Math.floor(Math.random() * 45)) + 0;
    		while (t[i] - t[i-1] > 5) {
    			t[i] = ((int) Math.floor(Math.random() * 45)) + 0;
    		}
    	}
        return t;
    }

    public static void calculaImprimeMedia(int[] temperaturas) {
        float mediaTemperaturas = media(temperaturas);
        System.out.println(mediaTemperaturas);
    }

    public static float media(int[] temperaturas) {
        int suma = 0;

        for (int i = 0; i < temperaturas.length; i++) {
            suma = suma + temperaturas[i];
        }
        float media = suma / temperaturas.length;
        return media;
    }

    public static void pintaGrafica(int[] temperaturas) {
        for (int i = 0; i < temperaturas.length; i++) {
            System.out.println(pinta("_", temperaturas[i]));
        }
    }
    

    public static String pinta(String simbolo, int numero) {
        String grafico = "";

        for (int i = 0; i < numero; i++) {
            grafico = grafico + simbolo;
        }
        return grafico;
    }
}