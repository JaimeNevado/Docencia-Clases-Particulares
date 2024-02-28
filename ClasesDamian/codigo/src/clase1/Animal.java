package clase1;

public class Animal {
	private String nombre;
	private int edad;
	private int peso;
	
	public Animal(String n, int e, int p) {
		this.nombre = n;
		this.edad = e;
		this.peso = p;
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
