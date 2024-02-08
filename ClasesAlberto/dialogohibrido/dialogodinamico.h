#ifndef DIALOGODINAMICO_H
#define DIALOGODINAMICO_H
#include "ui_dialogodinamico.h"

#include <QVector>
#include <QSpinBox>
#include <QHBoxLayout>
#include "widgetnota.h"

// #define NUM_NOTAS 5


class DialogoDinamico : public QDialog, public Ui::DialogoDinamico {
Q_OBJECT

public:
	static const int NUM_NOTAS = 5;
	
	DialogoDinamico(QWidget *parent = NULL);

	QVector<WidgetNota*> notas;

public slots:
	void slotBotonMedia();
	void slotBotonMaximo();
	void slotBotonMinimo();
};

#endif
