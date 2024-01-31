package clase11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class archivos {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/archivo.csv";
		
		BufferedReader reader = null;
		String line = "";
		
		int[] array = new int[3];
		int i = 0;
		try {
			reader = new BufferedReader (new FileReader(ruta));
			while ((line = reader.readLine()) != null) {
				String[] row = line.split(",");
				for (String s : row) {
					array[i] = Integer.parseInt(s);
					i++;
				}
			}
		} catch (Exception e) {
			System.out.println("Error");
		} finally {
			try { 
				reader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		// Print array
		for (int elemento : array) {
			System.out.print(elemento + " ");
		}
		
	}

}
