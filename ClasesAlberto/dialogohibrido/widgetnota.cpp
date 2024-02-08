#include "widgetnota.h"

WidgetNota::WidgetNota(QString titulo, QWidget *parent):QWidget(parent){
	setupUi(this);
	
	lblTitulo->setText(titulo);

}

float WidgetNota::valorNota(){

	return spbNota->value();
}

bool WidgetNota::activo(){

	if ( chkActivo->isChecked() )
		return true;
	else
		return false;
	
}
