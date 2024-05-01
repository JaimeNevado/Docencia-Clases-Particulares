package cartas;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Carta {
    private String nombre;
    private int numero;
    private String palo;

    public Carta(int numero, String palo) {
        this.numero = numero;
        this.palo = palo;
        generarNombre();
    }

    private void generarNombre() {
        if (numero >= 1 && numero <= 7) {
            nombre = String.valueOf(numero);
        } else {
            switch (numero) {
                case 8:
                    nombre = "SOTA";
                    break;
                case 9:
                    nombre = "CABALLO";
                    break;
                case 10:
                    nombre = "REY";
                    break;
            }
        }
        nombre += " de " + palo;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumero() {
        return numero;
    }

    public String getPalo() {
        return palo;
    }

    @Override
    public String toString() {
        return "(" + palo + ":" + nombre + ")";
    }
}