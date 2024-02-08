package clase12;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ej2 {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase12/archivo.csv";
		String ruta2 = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase12/archivo.txt";
		
		BufferedReader reader = null;
		BufferedWriter writer = null;
		
		try {
			reader = new BufferedReader(new FileReader(ruta));
			writer = new BufferedWriter(new FileWriter(ruta2));
			String linea = "";
			while ((linea = reader.readLine()) != null) {
				String[] array = linea.split(",");
				writer.write("El alumno "+ array[0] + " " + array[1]+ " ha sacado un " + array[2]);
							
				if (Integer.parseInt(array[2]) >= 5) {
					writer.write(" APROBADO\n");
				} else {
					writer.write(" SUSPENSO\n");
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
			try {
				writer.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}

	}

}
