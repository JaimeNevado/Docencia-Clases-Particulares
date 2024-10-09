package clase12;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ej3 {

	public static void main(String[] args) {

		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase12/archivo.csv";

		BufferedWriter writer = null;
		int array[] = { 2, 4, 7, 2, 9, 1, 5 };

		try {
			writer = new BufferedWriter(new FileWriter(ruta));
			for (int i = 0; i < array.length; i++) {
				writer.write(array[i] + ",");
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				writer.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

}
