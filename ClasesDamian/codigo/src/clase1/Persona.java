package clase1;

public class Persona {
	private int edad;
	private double altura;
	private String nombre;
	
	public Persona(int e, double altura, String nombre) {
		this.edad = e;
		this.altura = altura;
		this.nombre = nombre;
	}
	
	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void hablar(String mensaje) {
		System.out.print("Hola soy " + this.nombre + " ");
		System.out.println(mensaje);
	}
	

	@Override
	public String toString() {
		return "Tengo " + edad + " años, mido " + altura + ", me llamo " + nombre;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return false;
		}
		Persona otra = (Persona) o;
		if (otra.nombre == this.nombre) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		Persona primerHumano = new Persona(21, 1.70, "Roberto");
		Persona segundoHumano = new Persona(20, 1.70, "Roberto");
	
		
		
		System.out.println(primerHumano.equals(segundoHumano));

	}

}
