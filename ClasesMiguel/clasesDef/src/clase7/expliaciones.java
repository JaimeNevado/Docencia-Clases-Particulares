package clase7;

public class expliaciones {
	
	public static void comprobarnotas(String name, double[] notas) {
		double media = 0;
		double sumaNotas = 0;
		
		// {3, 5, 8, 9, 10, 3, 6}
        for (int i = 0; i < notas.length; i++){
        	if (notas[i] > 10) {
        		System.out.println("ERRRORRRRRRR");
        	}
            sumaNotas = sumaNotas + notas[i];
        }
        
        media = sumaNotas/notas.length;
        
        
        if (media < 0 ) {
            System.out.println("esto no hay quien lo arregle ");
        }else if (media < 5) {
            System.out.println("tu vas pal hoyo ");
        }else if (media == 5) {
            System.out.println("por los pelos de un calvo");
        }else if (media <= 10) {
            System.out.println("q te cagas aprobao");
        } else {
            System.out.println("pa la nasa " + name);
        }
    }


    public static void main(String[] args) {
    	double[] numeros = {3, 177, 8, 9, 10, 3, 6};
    	
    	comprobarnotas("jaime", numeros);

    }

}
