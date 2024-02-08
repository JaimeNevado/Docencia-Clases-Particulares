#ifndef WIDGETNOTA_H
#define WIDGETNOTA_H

#include "ui_widgetnota.h"

class WidgetNota : public QWidget, public Ui::WidgetNota {


public:
	WidgetNota(QString titulo, QWidget *parent = 0);
	
	float valorNota();
	
	bool activo();

};
#endif
