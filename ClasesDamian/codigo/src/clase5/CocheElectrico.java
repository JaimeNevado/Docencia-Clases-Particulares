package clase5;

class CocheElectrico extends Coche {
    // Constructor
	private int bateria = 0;
    public CocheElectrico(String marca, String modelo, String color, int bateriaInicial) {
        super(marca, modelo, color);
        bateria = bateriaInicial;
    }

    // Método adicional
    public void cargarBateria(int carga) {
    	if (this.bateria + carga <= 100) {
    		System.out.println(marca + " " + modelo + " está cargando la batería.");
    		this.bateria += carga;
    		System.out.println("Carga actual: " + this.bateria);    		
    	} else {
    		System.out.println("Si lo cargamos tanto la batería explota!!");
    	}
    }
}
