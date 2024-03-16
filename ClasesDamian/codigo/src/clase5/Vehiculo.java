package clase5;

class Vehiculo {
    // Atributos
    protected String marca;
    protected String modelo;
    protected String color;
    protected int velocidad;

    // Constructor
    public Vehiculo(String marca, String modelo, String color) {
        this.marca = marca;
        this.modelo = modelo;
        this.color = color;
        this.velocidad = 0;
    }

    // Métodos
    public void acelerar(int incremento) {
        velocidad += incremento;
    }

    public void frenar(int decremento) {
        velocidad -= decremento;
    }

    public void cambiarColor(String nuevoColor) {
        color = nuevoColor;
    }

    public String toString() {
        return "Vehículo: " + marca + " " + modelo + ", Color: " + color + ", Velocidad: " + velocidad + "km/h";
    }

    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (!(obj instanceof Vehiculo)) {
            return false;
        }
        Vehiculo vehiculo = (Vehiculo) obj;
        return marca.equals(vehiculo.marca) && modelo.equals(vehiculo.modelo) && color.equals(vehiculo.color);
    }
    
    
    
    
    }