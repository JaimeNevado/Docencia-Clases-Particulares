/********************************************************************************
** Form generated from reading UI file 'dialogodinamico.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOGODINAMICO_H
#define UI_DIALOGODINAMICO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_DialogoDinamico
{
public:
    QDialogButtonBox *buttonBox;
    QLabel *label;
    QGroupBox *grupoNotas;
    QPushButton *btnMedia;
    QLabel *labelMedia;
    QLabel *labelMaximo;
    QLabel *labelMinimo;
    QLabel *lblMedia;
    QLabel *lblMaximo;
    QLabel *lblMinimo;

    void setupUi(QDialog *DialogoDinamico)
    {
        if (DialogoDinamico->objectName().isEmpty())
            DialogoDinamico->setObjectName(QString::fromUtf8("DialogoDinamico"));
        DialogoDinamico->resize(496, 383);
        buttonBox = new QDialogButtonBox(DialogoDinamico);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setGeometry(QRect(130, 330, 341, 32));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        label = new QLabel(DialogoDinamico);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(40, 10, 311, 21));
        grupoNotas = new QGroupBox(DialogoDinamico);
        grupoNotas->setObjectName(QString::fromUtf8("grupoNotas"));
        grupoNotas->setGeometry(QRect(40, 70, 321, 151));
        btnMedia = new QPushButton(DialogoDinamico);
        btnMedia->setObjectName(QString::fromUtf8("btnMedia"));
        btnMedia->setGeometry(QRect(318, 264, 121, 31));
        labelMedia = new QLabel(DialogoDinamico);
        labelMedia->setObjectName(QString::fromUtf8("labelMedia"));
        labelMedia->setGeometry(QRect(50, 250, 67, 17));
        labelMaximo = new QLabel(DialogoDinamico);
        labelMaximo->setObjectName(QString::fromUtf8("labelMaximo"));
        labelMaximo->setGeometry(QRect(50, 280, 67, 17));
        labelMinimo = new QLabel(DialogoDinamico);
        labelMinimo->setObjectName(QString::fromUtf8("labelMinimo"));
        labelMinimo->setGeometry(QRect(50, 310, 67, 17));
        lblMedia = new QLabel(DialogoDinamico);
        lblMedia->setObjectName(QString::fromUtf8("lblMedia"));
        lblMedia->setGeometry(QRect(140, 250, 67, 17));
        lblMaximo = new QLabel(DialogoDinamico);
        lblMaximo->setObjectName(QString::fromUtf8("lblMaximo"));
        lblMaximo->setGeometry(QRect(140, 280, 67, 17));
        lblMinimo = new QLabel(DialogoDinamico);
        lblMinimo->setObjectName(QString::fromUtf8("lblMinimo"));
        lblMinimo->setGeometry(QRect(140, 310, 67, 17));

        retranslateUi(DialogoDinamico);
        QObject::connect(buttonBox, SIGNAL(accepted()), DialogoDinamico, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DialogoDinamico, SLOT(reject()));

        QMetaObject::connectSlotsByName(DialogoDinamico);
    } // setupUi

    void retranslateUi(QDialog *DialogoDinamico)
    {
        DialogoDinamico->setWindowTitle(QCoreApplication::translate("DialogoDinamico", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("DialogoDinamico", "Calculadora de medias, m\303\241ximos y m\303\255nimos", nullptr));
        grupoNotas->setTitle(QCoreApplication::translate("DialogoDinamico", "Notas", nullptr));
        btnMedia->setText(QCoreApplication::translate("DialogoDinamico", "Calcular Media", nullptr));
        labelMedia->setText(QCoreApplication::translate("DialogoDinamico", "Media", nullptr));
        labelMaximo->setText(QCoreApplication::translate("DialogoDinamico", "M\303\241ximo", nullptr));
        labelMinimo->setText(QCoreApplication::translate("DialogoDinamico", "M\303\255nimo", nullptr));
        lblMedia->setText(QCoreApplication::translate("DialogoDinamico", "0", nullptr));
        lblMaximo->setText(QCoreApplication::translate("DialogoDinamico", "0", nullptr));
        lblMinimo->setText(QCoreApplication::translate("DialogoDinamico", "0", nullptr));
    } // retranslateUi

};

namespace Ui {
    class DialogoDinamico: public Ui_DialogoDinamico {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOGODINAMICO_H
