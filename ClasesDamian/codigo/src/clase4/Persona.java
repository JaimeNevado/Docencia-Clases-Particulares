package clase4;

public class Persona {
	private int edad;
	private String nombre;
	private double altura;
	
	public Persona(int e, String n, double a) {
		this.edad = e;
		this.nombre = n;
		this.altura = a;
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

	@Override
	public String toString() {
        return this.nombre + " - " + this.edad + " años - " + this.altura + " metros";
    }

	@Override
	public boolean equals(Object obj) {
		Persona paco = (Persona) obj;
		
		if (this.nombre == paco.nombre && this.edad == paco.edad && this.altura == paco.altura) {
			return true;
		} else {
			return false;
		}
    }
	
	
	public static void main(String[] args) {
		Persona p1 = new Persona(19, "Manuel", 2.70);
		Persona p2 = new Persona(19, "Manuel", 2.70);
		
	
		
		System.out.println(p1);
		
		if (p1.equals(p2)) {
			System.out.println("Iguales");
		} else {
			System.out.println("Diferentes");
		}
		

	}

}
