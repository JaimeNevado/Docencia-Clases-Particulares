package clase1;

public class Animal {
	private String nombre;
	private int edad;
	private int peso;
	
	public Animal(int edad2, String nombre2, double altura) {
		this.nombre = edad2;
		this.edad = nombre2;
		this.peso = altura;
	}

	public void hacerRuido() {
		System.out.println("*Hace ruido épicamente*");
	}
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public int getPeso() {
		return peso;
	}

	public void setPeso(int peso) {
		this.peso = peso;
	}
	

}
