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
        frmConsulta.resize(453, 337)
        self.tblPersonas = QtWidgets.QTableView(frmConsulta)
        self.tblPersonas.setGeometry(QtCore.QRect(10, 30, 331, 261))
        self.tblPersonas.setAlternatingRowColors(True)
        self.tblPersonas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblPersonas.setObjectName("tblPersonas")
        self.tblPersonas.horizontalHeader().setDefaultSectionSize(97)
        self.btnConsultar = QtWidgets.QPushButton(frmConsulta)
        self.btnConsultar.setGeometry(QtCore.QRect(360, 20, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnConsultar.setFont(font)
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnBorrar = QtWidgets.QPushButton(frmConsulta)
        self.btnBorrar.setGeometry(QtCore.QRect(360, 100, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setObjectName("btnBorrar")
        self.btnActualizar = QtWidgets.QPushButton(frmConsulta)
        self.btnActualizar.setGeometry(QtCore.QRect(360, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnActualizar.setFont(font)
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnCerrar = QtWidgets.QPushButton(frmConsulta)
        self.btnCerrar.setGeometry(QtCore.QRect(360, 200, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCerrar.setFont(font)
        self.btnCerrar.setObjectName("btnCerrar")
        self.Persona = QtWidgets.QLabel(frmConsulta)
        self.Persona.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.Persona.setObjectName("Persona")
        self.btnAgregar = QtWidgets.QPushButton(frmConsulta)
        self.btnAgregar.setGeometry(QtCore.QRect(360, 140, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setObjectName("btnAgregar")
        self.Filtro = QtWidgets.QLabel(frmConsulta)
        self.Filtro.setGeometry(QtCore.QRect(20, 310, 31, 21))
        self.Filtro.setObjectName("Filtro")
        self.btnAplicarFiltro = QtWidgets.QPushButton(frmConsulta)
        self.btnAplicarFiltro.setGeometry(QtCore.QRect(270, 310, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btnAplicarFiltro.setFont(font)
        self.btnAplicarFiltro.setObjectName("btnAplicarFiltro")
        self.txtFiltro = QtWidgets.QLineEdit(frmConsulta)
        self.txtFiltro.setGeometry(QtCore.QRect(60, 310, 201, 20))
        self.txtFiltro.setObjectName("txtFiltro")

        self.retranslateUi(frmConsulta)
        QtCore.QMetaObject.connectSlotsByName(frmConsulta)

    def retranslateUi(self, frmConsulta):
        _translate = QtCore.QCoreApplication.translate
        frmConsulta.setWindowTitle(_translate("frmConsulta", "Consulta de Datos"))
        self.btnConsultar.setText(_translate("frmConsulta", "Consultar"))
        self.btnBorrar.setText(_translate("frmConsulta", "Borrar"))
        self.btnActualizar.setText(_translate("frmConsulta", "Actualizar"))
        self.btnCerrar.setText(_translate("frmConsulta", "Cerrar"))
        self.Persona.setText(_translate("frmConsulta", "Persona"))
        self.btnAgregar.setText(_translate("frmConsulta", "Agregar"))
        self.Filtro.setText(_translate("frmConsulta", "Filtro :"))
        self.btnAplicarFiltro.setText(_translate("frmConsulta", "Aplicar Filtro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConsulta = QtWidgets.QDialog()
    ui = Ui_frmConsulta()
    ui.setupUi(frmConsulta)
    frmConsulta.show()
    sys.exit(app.exec_())

