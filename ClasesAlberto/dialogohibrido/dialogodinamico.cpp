#include "dialogodinamico.h"
#include <QDebug>

DialogoDinamico::DialogoDinamico(QWidget *parent): QDialog(parent){
	setupUi(this);
	
	for (int i=0; i<NUM_NOTAS; i++){
		//QSpinBox * nuevoSpinBox = new QSpinBox;
		WidgetNota *unaNota = new WidgetNota(QString("Nota ")+ QString::number(i));
		notas.append(unaNota);
	}
	
	QHBoxLayout *layout = new QHBoxLayout();
	
	for (int i=0; i<NUM_NOTAS; i++){
		layout->addWidget(notas.at(i));
	}
	
	grupoNotas->setLayout(layout);
	grupoNotas->adjustSize();
	
	connect(btnMedia, SIGNAL(clicked()), this, SLOT(slotBotonMedia()));
	connect(btnMedia, SIGNAL(clicked()), this, SLOT(slotBotonMaximo()));
	connect(btnMedia, SIGNAL(clicked()), this, SLOT(slotBotonMinimo()));
}

void DialogoDinamico::slotBotonMedia() {

	int acumulador = 0;
	int totalnotas = 0;
	for (int i=0; i<notas.size(); i++){
		WidgetNota *unaNota = notas.at(i);
		if (unaNota->activo())
		{
			acumulador += unaNota->valorNota();
			totalnotas++;
		}
	}
	int media = acumulador / totalnotas;
	lblMedia->setText(QString::number(media)); 
}

void DialogoDinamico::slotBotonMaximo() {

	int maximo = 0;
	for (int i=0; i<notas.size(); i++){
		WidgetNota *unaNota = notas.at(i);
		if (unaNota->activo())
		    if (unaNota->spbNota->value() > maximo)
			maximo = unaNota->valorNota();
	}
	
	lblMaximo->setText(QString::number(maximo)); 
}

void DialogoDinamico::slotBotonMinimo() {
	int minimo = 10;
	for (int i=0; i<notas.size(); i++){
		WidgetNota * unaNota = notas.at(i);
		if (unaNota->activo())
		   if (unaNota->spbNota->value() < minimo)
			minimo = unaNota->valorNota();
	}
	
	lblMinimo->setText(QString::number(minimo)); 
}

