/********************************************************************************
** Form generated from reading UI file 'widgetnota.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGETNOTA_H
#define UI_WIDGETNOTA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_WidgetNota
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *lblTitulo;
    QSpinBox *spbNota;
    QCheckBox *chkActivo;

    void setupUi(QWidget *WidgetNota)
    {
        if (WidgetNota->objectName().isEmpty())
            WidgetNota->setObjectName(QString::fromUtf8("WidgetNota"));
        WidgetNota->resize(112, 122);
        verticalLayout = new QVBoxLayout(WidgetNota);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        lblTitulo = new QLabel(WidgetNota);
        lblTitulo->setObjectName(QString::fromUtf8("lblTitulo"));

        verticalLayout->addWidget(lblTitulo);

        spbNota = new QSpinBox(WidgetNota);
        spbNota->setObjectName(QString::fromUtf8("spbNota"));

        verticalLayout->addWidget(spbNota);

        chkActivo = new QCheckBox(WidgetNota);
        chkActivo->setObjectName(QString::fromUtf8("chkActivo"));

        verticalLayout->addWidget(chkActivo);


        retranslateUi(WidgetNota);

        QMetaObject::connectSlotsByName(WidgetNota);
    } // setupUi

    void retranslateUi(QWidget *WidgetNota)
    {
        WidgetNota->setWindowTitle(QCoreApplication::translate("WidgetNota", "Form", nullptr));
        lblTitulo->setText(QCoreApplication::translate("WidgetNota", "Nota", nullptr));
        chkActivo->setText(QCoreApplication::translate("WidgetNota", "Activo", nullptr));
    } // retranslateUi

};

namespace Ui {
    class WidgetNota: public Ui_WidgetNota {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGETNOTA_H
