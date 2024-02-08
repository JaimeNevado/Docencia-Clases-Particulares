#include <QApplication>
#include "dialogodinamico.h"

int main(int argc, char *argv[])
{
	QApplication app(argc, argv);
	DialogoDinamico *dialogoDinamico = new DialogoDinamico;
	dialogoDinamico->show();
	return app.exec();
}
