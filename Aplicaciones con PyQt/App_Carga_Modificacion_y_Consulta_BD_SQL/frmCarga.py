# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCarga.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmCarga(object):
    def setupUi(self, frmCarga):
        frmCarga.setObjectName("frmCarga")
        frmCarga.setWindowModality(QtCore.Qt.WindowModal)
        frmCarga.resize(354, 104)
        self.Numero = QtWidgets.QLabel(frmCarga)
        self.Numero.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.Numero.setObjectName("Numero")
        self.Nombre = QtWidgets.QLabel(frmCarga)
        self.Nombre.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.Nombre.setObjectName("Nombre")
        self.Clase = QtWidgets.QLabel(frmCarga)
        self.Clase.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.Clase.setObjectName("Clase")
        self.txtNumero = QtWidgets.QLineEdit(frmCarga)
        self.txtNumero.setGeometry(QtCore.QRect(80, 10, 81, 20))
        self.txtNumero.setMaxLength(5)
        self.txtNumero.setObjectName("txtNumero")
        self.txtNombre = QtWidgets.QLineEdit(frmCarga)
        self.txtNombre.setGeometry(QtCore.QRect(80, 40, 151, 20))
        self.txtNombre.setMaxLength(50)
        self.txtNombre.setObjectName("txtNombre")
        self.btnAceptar = QtWidgets.QPushButton(frmCarga)
        self.btnAceptar.setGeometry(QtCore.QRect(260, 20, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnCerrar = QtWidgets.QPushButton(frmCarga)
        self.btnCerrar.setGeometry(QtCore.QRect(260, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCerrar.setFont(font)
        self.btnCerrar.setObjectName("btnCerrar")
        self.spnClase = QtWidgets.QSpinBox(frmCarga)
        self.spnClase.setGeometry(QtCore.QRect(80, 70, 81, 21))
        self.spnClase.setMinimum(1900)
        self.spnClase.setMaximum(2021)
        self.spnClase.setObjectName("spnClase")

        self.retranslateUi(frmCarga)
        QtCore.QMetaObject.connectSlotsByName(frmCarga)

    def retranslateUi(self, frmCarga):
        _translate = QtCore.QCoreApplication.translate
        frmCarga.setWindowTitle(_translate("frmCarga", "Carga de Datos"))
        self.Numero.setText(_translate("frmCarga", "Número:"))
        self.Nombre.setText(_translate("frmCarga", "Nombre:"))
        self.Clase.setText(_translate("frmCarga", "Clase:"))
        self.btnAceptar.setText(_translate("frmCarga", "Aceptar"))
        self.btnCerrar.setText(_translate("frmCarga", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCarga = QtWidgets.QDialog()
    ui = Ui_frmCarga()
    ui.setupUi(frmCarga)
    frmCarga.show()
    sys.exit(app.exec_())

