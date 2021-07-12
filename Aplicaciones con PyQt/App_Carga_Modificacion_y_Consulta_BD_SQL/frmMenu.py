# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMenu(object):
    def setupUi(self, frmMenu):
        frmMenu.setObjectName("frmMenu")
        frmMenu.setWindowModality(QtCore.Qt.WindowModal)
        frmMenu.resize(403, 199)
        self.centralwidget = QtWidgets.QWidget(frmMenu)
        self.centralwidget.setObjectName("centralwidget")
        frmMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivos = QtWidgets.QMenu(self.menubar)
        self.menuArchivos.setObjectName("menuArchivos")
        frmMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmMenu)
        self.statusbar.setObjectName("statusbar")
        frmMenu.setStatusBar(self.statusbar)
        self.actionCarga_de_Datos = QtWidgets.QAction(frmMenu)
        self.actionCarga_de_Datos.setObjectName("actionCarga_de_Datos")
        self.actionConsulta_de_Datos = QtWidgets.QAction(frmMenu)
        self.actionConsulta_de_Datos.setObjectName("actionConsulta_de_Datos")
        self.actionSalir = QtWidgets.QAction(frmMenu)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivos.addAction(self.actionCarga_de_Datos)
        self.menuArchivos.addAction(self.actionConsulta_de_Datos)
        self.menuArchivos.addSeparator()
        self.menuArchivos.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivos.menuAction())

        self.retranslateUi(frmMenu)
        QtCore.QMetaObject.connectSlotsByName(frmMenu)

    def retranslateUi(self, frmMenu):
        _translate = QtCore.QCoreApplication.translate
        frmMenu.setWindowTitle(_translate("frmMenu", "Formulario de Inicio"))
        self.menuArchivos.setTitle(_translate("frmMenu", "Archivos"))
        self.actionCarga_de_Datos.setText(_translate("frmMenu", "Carga de Datos"))
        self.actionConsulta_de_Datos.setText(_translate("frmMenu", "Consulta de Datos"))
        self.actionSalir.setText(_translate("frmMenu", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMenu = QtWidgets.QMainWindow()
    ui = Ui_frmMenu()
    ui.setupUi(frmMenu)
    frmMenu.show()
    sys.exit(app.exec_())

