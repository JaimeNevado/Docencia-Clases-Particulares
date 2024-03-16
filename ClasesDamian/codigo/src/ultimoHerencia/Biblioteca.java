package ultimoHerencia;

public class Biblioteca {
    private MaterialBiblioteca[] materiales;

    public Biblioteca(int capacidad) {
        this.materiales = new MaterialBiblioteca[capacidad];
    }

    public void agregarMaterial(MaterialBiblioteca material, int indice) {
        this.materiales[indice] = material;
    }

    public MaterialBiblioteca[] getMateriales() {
		return materiales;
	}

	public void setMateriales(MaterialBiblioteca[] materiales) {
		this.materiales = materiales;
	}

	public MaterialBiblioteca buscarMaterial(String titulo) {
        for (MaterialBiblioteca material : this.materiales) {
            if (material != null && material.getTitulo().equals(titulo)) {
                return material;
            }
        }
        return null;
    }

}