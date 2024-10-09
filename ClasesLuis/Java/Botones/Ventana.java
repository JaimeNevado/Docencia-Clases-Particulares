package Botones;

import javax.swing.*;
import java.awt.*;

public class Ventana extends JFrame {
    private JPanel panel;
    public Ventana(){
        setSize(1000, 1000);  //Tamaño de la ventana
        setTitle("APP de Finanzas por Jaime");
        setDefaultCloseOperation(EXIT_ON_CLOSE);    // Cerrar la ventana al cerrar

        //setLocation(100, 200);  // Para ponerlo en una posicion específica
        setLocationRelativeTo(null); // Para ponerlo en el centro justo

        /* Extras para añadir */
        setResizable(false);    // Indicamos si se puede reescalar la ventana
        setMinimumSize(new Dimension(200, 200));    // Establecemos tamaño mínimo
        getContentPane().setBackground(Color.BLUE);     // Color de fondo
        /* Extras para añadir */

        iniciarComponentes();
        //colocarPaneles();
        colocarBotones();
    }

    private void colocarPaneles(){
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);
    }
    private void iniciarComponentes(){
        // Necesitamos un panel para añadir todas las cosas (es como el papel encima del escritorio)
        panel = new JPanel();

        // Desactivar el layout por defecto del panel
        panel.setLayout(null);

        // panel.setBackground(Color.GREEN);   // Establecemos el color del panel para poder verlo
        this.getContentPane().add(panel);   // A lo que haya en la ventana, le añadimos el panel

        JLabel etiqueta = new JLabel();   // Creamos una etiqueta
        etiqueta.setText("Hola Mundo");     // Le añadimos texto a la etiqueta que hemos creado
                                            // aunque se puede hacer directamente en el constructor

        etiqueta.setForeground(Color.blue); // Establezemos el color de la letra
        etiqueta.setBounds(this.getWidth()/2 - 40, 0, 150, 40);     // Posiciono la etiqueta en una posicion
                                                                    // Si no hago un setLayout(null), se queda igual

        panel.add(etiqueta);
    }


    private void colocarBotones(){
        JButton boton1 = new JButton("OK");
        boton1.setBounds(100, 100, 100, 40);

        JLabel etiqueta = new JLabel();   // Creamos una etiqueta
        etiqueta.setText("AHAHAHAH");     // Le añadimos texto a la etiqueta que hemos creado
        // aunque se puede hacer directamente en el constructor

        etiqueta.setForeground(Color.blue); // Establezemos el color de la letra
        etiqueta.setBounds(200, 200, 150, 40);     // Posiciono la etiqueta en una posicion
        // Si no hago un setLayout(null), se queda igual


        // Añadir ActionListener al boton1
        boton1.addActionListener(e -> {
            JOptionPane.showMessageDialog(null, "Pulsaste el botón OK");
            System.out.println("Hola, si se ha pulsado colega");
            panel.add(etiqueta);
            panel.revalidate();      // Revalida el panel para que se actualice su estructura
            panel.repaint();
        });

       panel.add(boton1);
    }
}
