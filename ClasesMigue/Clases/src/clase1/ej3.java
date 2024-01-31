package clase1;

public class ej3 {

	public static void main(String[] args) {
		int combustible = 1000;
        int numeroMotores = 3;
        int tripulacion = 3;
        String palabraClave = "Mantequilla";

        if (combustible == 1000 && numeroMotores == 3 && tripulacion == 3 && palabraClave == "Mantequilla") {
            System.out.println("Condiciones verificadas. Autorización para el lanzamiento del cohete.");
        } else {
            System.out.println("No se cumplen todas las condiciones. Lanzamiento no autorizado.");
        }
	}

}


