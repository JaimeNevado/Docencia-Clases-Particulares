package clase5;

// Ejercicio 3
public class Main {
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla", "Rojo");
        coche1.abrirPuertas();

        Motocicleta moto1 = new Motocicleta("Honda", "CBR500R", "Negro");
        moto1.hacerAcrobacias();

        CocheElectrico cocheElectrico1 = new CocheElectrico("Tesla", "Model S", "Blanco", 100);
        cocheElectrico1.cargarBateria(20);

        System.out.println(coche1);
    }
}