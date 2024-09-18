package clase2;

import java.util.Objects;

public class Persona {
	
	// atributos
	private int edad;
	private float altura;
	private String nombre;
	
	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public float getAltura() {
		return altura;
	}

	public void setAltura(float altura) {
		this.altura = altura;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void saludar() {
		System.out.println("Hola este codigo es muy complicado");
	}
	
	
	
	
	@Override
	public String toString() {
		return "Edad=" + edad + "\nAltura=" + altura + "\nNombre=" + nombre;
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Persona other = (Persona) obj;
		return altura == other.altura && edad == other.edad
				&& Objects.equals(nombre, other.nombre);
	}

	public Persona (int e, float a, String n) {
		this.edad = e;
		this.altura = a;
		this.nombre = n;
	}

	
	public static void main(String[] args) {
		Persona nuevaPersona = new Persona(21, 10, "Maikel");	// -> #12	
		Persona otraPersona = new Persona(21, 10, "Maikel");	// -> #16
		
		if (nuevaPersona.equals(otraPersona)) {
			System.out.println("Son iguales");
		} else {
			System.out.println("NO son iguales");
		}
		
	}
}
