package clase4;

import clase1.Animal;

public class Perro extends Animal {
	private String colorPelaje;
	
	public Perro(int edad, String nombre, int altura, String colorPelaje) {
		super(edad, nombre, altura);
		this.colorPelaje = colorPelaje;
	}


	public static void main(String[] args) {
		Perro snoppy = new Perro(2, "Juan", 1, "Marron");
		

	}

}
