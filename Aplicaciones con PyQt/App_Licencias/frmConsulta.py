# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmConsulta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmConsulta(object):
    def setupUi(self, frmConsulta):
        frmConsulta.setObjectName("frmConsulta")
        frmConsulta.resize(655, 414)
        self.btnConsultar = QtWidgets.QPushButton(frmConsulta)
        self.btnConsultar.setGeometry(QtCore.QRect(550, 20, 81, 31))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnSalir = QtWidgets.QPushButton(frmConsulta)
        self.btnSalir.setGeometry(QtCore.QRect(550, 70, 81, 31))
        self.btnSalir.setObjectName("btnSalir")
        self.tblLicencias = QtWidgets.QTableView(frmConsulta)
        self.tblLicencias.setGeometry(QtCore.QRect(10, 60, 521, 291))
        self.tblLicencias.setObjectName("tblLicencias")
        self.cmbTipo = QtWidgets.QComboBox(frmConsulta)
        self.cmbTipo.setGeometry(QtCore.QRect(120, 20, 281, 22))
        self.cmbTipo.setObjectName("cmbTipo")
        self.label_2 = QtWidgets.QLabel(frmConsulta)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(frmConsulta)
        self.label.setGeometry(QtCore.QRect(30, 370, 71, 16))
        self.label.setObjectName("label")
        self.txtTotal = QtWidgets.QLineEdit(frmConsulta)
        self.txtTotal.setGeometry(QtCore.QRect(110, 370, 113, 20))
        self.txtTotal.setObjectName("txtTotal")

        self.retranslateUi(frmConsulta)
        QtCore.QMetaObject.connectSlotsByName(frmConsulta)

    def retranslateUi(self, frmConsulta):
        _translate = QtCore.QCoreApplication.translate
        frmConsulta.setWindowTitle(_translate("frmConsulta", "Consulta de Licencias"))
        self.btnConsultar.setText(_translate("frmConsulta", "&Consultar"))
        self.btnSalir.setText(_translate("frmConsulta", "&Salir"))
        self.label_2.setText(_translate("frmConsulta", "Tipo de Licencia"))
        self.label.setText(_translate("frmConsulta", "Total de Días"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConsulta = QtWidgets.QDialog()
    ui = Ui_frmConsulta()
    ui.setupUi(frmConsulta)
    frmConsulta.show()
    sys.exit(app.exec_())

