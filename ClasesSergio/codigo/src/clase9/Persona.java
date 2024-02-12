package clase9;

public class Persona {
	
	private int edad;
	private String nombre;
	private double altura;
	
	public Persona(int edad, String nombre, double altura) {
		this.edad = edad;
		this.nombre = nombre;
		this.altura = altura;
	}
	
	public void saludar() {
		System.out.println("Hola me llamo " + this.nombre);
	}
	
	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	public static void main(String[] args) {
		
		Persona persona1 = new Persona(20, "Jaime", 1.80);		
		
		System.out.println("El nombre es: " + persona1.getNombre());
		// Salida => El nombre es: Jaime
		
		persona1.setNombre("Manuel");
		
		System.out.println("El nombre es: " + persona1.getNombre());
		// Salida => El nombre es: Manuel
		
		
	}

}
