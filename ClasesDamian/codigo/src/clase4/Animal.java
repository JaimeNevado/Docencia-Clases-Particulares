package clase4;

public abstract class Animal {
	private int edad;
	private String nombre;
	private int altura;
	
	public Animal(int edad, String nombre, int altura) {
		this.edad = edad;
		this.nombre = nombre;
		this.altura = altura;
	}
	
	public void hacerRuido() {
		System.out.println("Soy un animal haciendo ruido!! ");
	}
	
	public void comer() {
		System.out.println("Soy un animal comiendo rico!! ");
	}
	
	
}
