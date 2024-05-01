package cartas;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


class Main {
    private LinkedList<Carta> baraja;
    private List<LinkedList<Carta>> mesas;
    private int turnos;

    public Main() {
        baraja = new LinkedList<>();
        mesas = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            mesas.add(new LinkedList<>());
        }
        inicializarBaraja();
        turnos = 0;
    }

    private void inicializarBaraja() {
        String[] palos = {"oros", "bastos", "espadas", "copas"};
        for (String palo : palos) {
            for (int i = 1; i <= 10; i++) {
                baraja.add(new Carta(i, palo));
            }
        }
        // Barajar la baraja
        java.util.Collections.shuffle(baraja);
    }

    public void jugar() {
        while (!baraja.isEmpty() && !juegoCompleto()) {
            turnos++;
            if (turnos == 1) {
                primeraVez();
            } else {
                siguienteTurno();
            }
        }
        System.out.println("Número de turnos empleados para resolverlo: " + turnos);
    }

    private void primeraVez() {
        Carta carta = baraja.poll();
        while (carta.getNumero() != 1) {
            baraja.addLast(carta);
            carta = baraja.poll();
        }
        mesas.get(0).addLast(carta);
        System.out.println("Roba la primera carta de la baraja: " + carta);
        mostrarMesas();
    }

    private void siguienteTurno() {
        Carta carta = baraja.poll();
        for (LinkedList<Carta> mesa : mesas) {
            if (!mesa.isEmpty()) {
                Carta ultimaCarta = mesa.getLast();
                if (carta.getNumero() == ultimaCarta.getNumero() + 1 && carta.getPalo().equals(ultimaCarta.getPalo())) {
                    mesa.addLast(carta);
                    System.out.println("Roba otra carta: " + carta);
                    mostrarMesas();
                    return;
                }
            }
        }
        baraja.addLast(carta);
        System.out.println("Roba otra carta: " + carta);
    }

    private boolean juegoCompleto() {
        for (LinkedList<Carta> mesa : mesas) {
            if (mesa.size() < 10) {
                return false;
            }
        }
        return true;
    }

    private void mostrarMesas() {
        for (int i = 0; i < mesas.size(); i++) {
            System.out.print("Cartas de " + mesas.get(i).getFirst().getPalo() + ": ");
            System.out.println(mesas.get(i));
        }
    }
}

