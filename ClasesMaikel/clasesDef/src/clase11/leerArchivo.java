package clase11;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class leerArchivo {

	public static void main(String[] args) {

		String ruta2 = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/archivo_salida.csv";

		String ruta = "C://miCarpeta/miArchivo.csv";

		BufferedWriter writer = null;

		try {
			writer = new BufferedWriter(new FileWriter(ruta));
			writer.write("Hola Mundo");
			writer.newLine();
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
