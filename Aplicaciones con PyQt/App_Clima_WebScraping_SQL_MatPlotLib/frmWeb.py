# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmWeb.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmWeb(object):
    def setupUi(self, frmWeb):
        frmWeb.setObjectName("frmWeb")
        frmWeb.resize(754, 607)
        self.centralwidget = QtWidgets.QWidget(frmWeb)
        self.centralwidget.setObjectName("centralwidget")
        self.browser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(10, 40, 731, 221))
        self.browser.setUrl(QtCore.QUrl("about:blank"))
        self.browser.setObjectName("browser")
        self.tblClima = QtWidgets.QTableView(self.centralwidget)
        self.tblClima.setGeometry(QtCore.QRect(10, 270, 391, 271))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tblClima.setFont(font)
        self.tblClima.setLineWidth(0)
        self.tblClima.setAlternatingRowColors(True)
        self.tblClima.setObjectName("tblClima")
        self.tblClima.horizontalHeader().setDefaultSectionSize(74)
        self.btnCargar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCargar.setGeometry(QtCore.QRect(640, 10, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCargar.setFont(font)
        self.btnCargar.setObjectName("btnCargar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(620, 270, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnConsultar.setFont(font)
        self.btnConsultar.setObjectName("btnConsultar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(400, 290, 351, 251))
        self.widget.setObjectName("widget")
        self.Facha = QtWidgets.QLabel(self.centralwidget)
        self.Facha.setGeometry(QtCore.QRect(410, 270, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Facha.setFont(font)
        self.Facha.setObjectName("Facha")
        self.cmbFecha = QtWidgets.QComboBox(self.centralwidget)
        self.cmbFecha.setGeometry(QtCore.QRect(450, 270, 151, 22))
        self.cmbFecha.setObjectName("cmbFecha")
        frmWeb.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmWeb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName("menubar")
        frmWeb.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmWeb)
        self.statusbar.setObjectName("statusbar")
        frmWeb.setStatusBar(self.statusbar)

        self.retranslateUi(frmWeb)
        QtCore.QMetaObject.connectSlotsByName(frmWeb)

    def retranslateUi(self, frmWeb):
        _translate = QtCore.QCoreApplication.translate
        frmWeb.setWindowTitle(_translate("frmWeb", "Pronostico del Tiempo"))
        self.btnCargar.setText(_translate("frmWeb", "&Cargar Pagina"))
        self.btnConsultar.setText(_translate("frmWeb", "Consultar"))
        self.Facha.setText(_translate("frmWeb", "Fecha"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmWeb = QtWidgets.QMainWindow()
    ui = Ui_frmWeb()
    ui.setupUi(frmWeb)
    frmWeb.show()
    sys.exit(app.exec_())

