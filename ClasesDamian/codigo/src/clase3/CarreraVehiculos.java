package clase3;

package clase3;

import java.util.Random;
import java.util.Scanner;

abstract class Vehiculo {
    String nombre;
    int posx;
    int posy;

    public abstract void avanzar();
    public abstract void retroceder();
}

class Coche extends Vehiculo {
    public Coche() {
        this.nombre = "COCHE";
        this.posx = 0;
        this.posy = 0;
    }

    @Override
    public void avanzar() {
        this.posx += 3;
    }

    @Override
    public void retroceder() {
        this.posx -= 3;
    }
}

class Moto extends Vehiculo {
    public Moto() {
        this.nombre = "MOTO";
        this.posx = 1;
        this.posy = 0;
    }

    @Override
    public void avanzar() {
        this.posx += 4;
    }

    @Override
    public void retroceder() {
        this.posx -= 4;
    }
}

class Camion extends Vehiculo {
    public Camion() {
        this.nombre = "CAMION";
        this.posx = 2;
        this.posy = 0;
    }

    @Override
    public void avanzar() {
        this.posx += 2;
    }

    @Override
    public void retroceder() {
        this.posx -= 2;
    }
}

public class CarreraVehiculos {
    static Scanner scanner = new Scanner(System.in);
    static Vehiculo[] vehiculos = {new Camion(), new Moto(), new Coche()};
    static String[] cartasObjetivo = {"Camion primero y Moto segundo", "Camion segundo y coche primero", "Camion tercero y moto primero"};
    static int[] mazoCartas = new int[10]; // 0 para avanzar, 1 para retroceder

    public static void main(String[] args) {
        generarMazoCartas();
        mostrarObjetivos();

        while (true) {
            for (int i = 0; i < vehiculos.length; i++) {
                jugarTurno(vehiculos[i], i);
                mostrarPista();
                if (haLlegadoPrimero()) {
                    System.out.println("¡El vehículo " + vehiculos[i].nombre + " ha ganado!");
                    System.exit(0);
                }
            }
        }
    }

    public static void generarMazoCartas() {
        Random random = new Random();
        for (int i = 0; i < mazoCartas.length; i++) {
            mazoCartas[i] = random.nextInt(2); // 0 para avanzar, 1 para retroceder
        }
    }

    public static void mostrarObjetivos() {
        System.out.println("Carta objetivo");
        for (int i = 0; i < vehiculos.length; i++) {
            System.out.println("El objetivo del " + vehiculos[i].nombre.toLowerCase() + " es: " + cartasObjetivo[i]);
        }
    }

    public static void mostrarPista() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 10; j++) {
                if (vehiculos[i].posx == j && vehiculos[i].posy == 0) {
                    System.out.print(vehiculos[i].nombre + " ");
                } else {
                    System.out.print("_ ");
                }
            }
            System.out.println();
        }
    }

    public static void jugarTurno(Vehiculo vehiculo, int indiceVehiculo) {
        System.out.println(vehiculo.nombre + " coge carta");
        System.out.println("Quien quieres que " + vehiculo.nombre.toLowerCase() + " avance: 1.camion 2.moto 3.coche");
        int vehiculoAvance = scanner.nextInt();
        if (mazoCartas[indiceVehiculo] == 0) {
            switch (vehiculoAvance) {
                case 1:
                    vehiculos[0].avanzar();
                    break;
                case 2:
                    vehiculos[1].avanzar();
                    break;
                case 3:
                    vehiculos[2].avanzar();
                    break;
            }
        } else {
            switch (vehiculoAvance) {
                case 1:
                    vehiculos[0].retroceder();
                    break;
                case 2:
                    vehiculos[1].retroceder();
                    break;
                case 3:
                    vehiculos[2].retroceder();
                    break;
            }
        }
    }

    public static boolean haLlegadoPrimero() {
        return vehiculos[0].posx >= 10 || vehiculos[1].posx >= 10 || vehiculos[2].posx >= 10;
    }
}
