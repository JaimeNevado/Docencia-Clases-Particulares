package PracticaParking;

public class Coche {
	private String matricula;
	private int horaEntrada;
	private int horaSalida;

	public Coche(String matricula, int horaEntrada, int horaSalida) {
		this.matricula = matricula;
		this.horaEntrada = horaEntrada;
		this.horaSalida = horaSalida;
	}

	public String getMatricula() {
		return matricula;
	}

	public int getHoraEntrada() {
		return horaEntrada;
	}

	public int getHoraSalida() {
		return horaSalida;
	}

	public void setHoraSalida(int horaSalida) {
		this.horaSalida = horaSalida;
	}
}