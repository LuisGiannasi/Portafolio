# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmIncendios.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmIncendios(object):
    def setupUi(self, frmIncendios):
        frmIncendios.setObjectName("frmIncendios")
        frmIncendios.resize(810, 591)
        self.centralwidget = QtWidgets.QWidget(frmIncendios)
        self.centralwidget.setObjectName("centralwidget")
        self.tblIncendiosProvincias = QtWidgets.QTableView(self.centralwidget)
        self.tblIncendiosProvincias.setGeometry(QtCore.QRect(10, 30, 791, 161))
        self.tblIncendiosProvincias.setSortingEnabled(True)
        self.tblIncendiosProvincias.setObjectName("tblIncendiosProvincias")
        self.txtCantidad = QtWidgets.QLabel(self.centralwidget)
        self.txtCantidad.setGeometry(QtCore.QRect(40, 0, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtCantidad.setFont(font)
        self.txtCantidad.setObjectName("txtCantidad")
        self.txtProvincia = QtWidgets.QLabel(self.centralwidget)
        self.txtProvincia.setGeometry(QtCore.QRect(20, 200, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtProvincia.setFont(font)
        self.txtProvincia.setObjectName("txtProvincia")
        self.cmbProvincias = QtWidgets.QComboBox(self.centralwidget)
        self.cmbProvincias.setGeometry(QtCore.QRect(90, 200, 251, 22))
        self.cmbProvincias.setObjectName("cmbProvincias")
        self.chkGraficar = QtWidgets.QCheckBox(self.centralwidget)
        self.chkGraficar.setGeometry(QtCore.QRect(360, 200, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkGraficar.setFont(font)
        self.chkGraficar.setObjectName("chkGraficar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 230, 791, 311))
        self.widget.setObjectName("widget")
        frmIncendios.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmIncendios)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        frmIncendios.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmIncendios)
        self.statusbar.setObjectName("statusbar")
        frmIncendios.setStatusBar(self.statusbar)

        self.retranslateUi(frmIncendios)
        QtCore.QMetaObject.connectSlotsByName(frmIncendios)

    def retranslateUi(self, frmIncendios):
        _translate = QtCore.QCoreApplication.translate
        frmIncendios.setWindowTitle(_translate("frmIncendios", "Consultas de Incendios"))
        self.txtCantidad.setText(_translate("frmIncendios", "Cantidad de incendios por provincia"))
        self.txtProvincia.setText(_translate("frmIncendios", "Provincia:"))
        self.chkGraficar.setText(_translate("frmIncendios", "Graficar todas las cantidades"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmIncendios = QtWidgets.QMainWindow()
    ui = Ui_frmIncendios()
    ui.setupUi(frmIncendios)
    frmIncendios.show()
    sys.exit(app.exec_())

