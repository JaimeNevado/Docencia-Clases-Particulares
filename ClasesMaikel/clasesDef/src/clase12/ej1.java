package clase12;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ej1 {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase12/archivo.csv";
		
		BufferedReader reader = null;
		
		try {
			reader = new BufferedReader(new FileReader(ruta));
			String linea = "";
			while ((linea = reader.readLine()) != null) {
				String[] array = linea.split(",");
				System.out.print("El alumno "+ array[0] + " " + array[1]+ " ha sacado un " + array[2]);
							
				if (Integer.parseInt(array[2]) >= 5) {
					System.out.println(" APROBADO");
				} else {
					System.out.println(" SUSPENSO");
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				reader.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}

}
