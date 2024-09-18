package clase1;

public class Persona {
	
	private int edad;
	private float peso;
	private String nombre;
	
	public void saludar() {
		System.out.println("Hola soy " + this.nombre + " y tengo " + this.edad + " años!!");
	}
	
	@Override
	public String toString() {
		return "Nombre: " + this.nombre + "\nEdad: " + this.edad + " años";
	}
	
	// Constructor
	public Persona (String n, int edad, float peso) {
		this.nombre = n;
		this.edad = edad;
		this.peso = peso;
	}
	
	

	public static void main(String[] args) {
		Persona memecoin = new Persona("Jaime", 19, 88);
		Persona pressBanca = new Persona("Maikel", 20, 190);
		
		
		System.out.println(memecoin);
		System.out.println(pressBanca);
	}

}

