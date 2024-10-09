package clase11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class archivos {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/archivo.csv";
		
		BufferedReader reader = null;
		String line = "";
		
		int[][] array = new int[3][3];
		try {
			int i = 0;
			int j = 0;
			reader = new BufferedReader (new FileReader(ruta));
			while ((line = reader.readLine()) != null) {
				String[] row = line.split(",");
				j = 0;
				for (String s : row) {
					array[i][j] = Integer.parseInt(s);
					j++;
				}
				i++;
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
		
		
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array[i].length; j++) {
				System.out.print(array[i][j] + " ");
			}
			System.out.println();
		}
		
	}

}
