# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmConsumo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmConsumo(object):
    def setupUi(self, frmConsumo):
        frmConsumo.setObjectName("frmConsumo")
        frmConsumo.resize(393, 435)
        self.centralwidget = QtWidgets.QWidget(frmConsumo)
        self.centralwidget.setObjectName("centralwidget")
        self.lblAreas = QtWidgets.QLabel(self.centralwidget)
        self.lblAreas.setGeometry(QtCore.QRect(30, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAreas.setFont(font)
        self.lblAreas.setObjectName("lblAreas")
        self.lblAreas_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblAreas_2.setGeometry(QtCore.QRect(30, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAreas_2.setFont(font)
        self.lblAreas_2.setObjectName("lblAreas_2")
        self.lblDispo = QtWidgets.QLabel(self.centralwidget)
        self.lblDispo.setGeometry(QtCore.QRect(180, 8, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblDispo.setFont(font)
        self.lblDispo.setObjectName("lblDispo")
        self.lblConsumoWh = QtWidgets.QLabel(self.centralwidget)
        self.lblConsumoWh.setGeometry(QtCore.QRect(180, 68, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblConsumoWh.setFont(font)
        self.lblConsumoWh.setObjectName("lblConsumoWh")
        self.lstAreas = QtWidgets.QListWidget(self.centralwidget)
        self.lstAreas.setGeometry(QtCore.QRect(30, 30, 131, 81))
        self.lstAreas.setObjectName("lstAreas")
        self.tblRegistrado = QtWidgets.QTableWidget(self.centralwidget)
        self.tblRegistrado.setGeometry(QtCore.QRect(30, 150, 331, 192))
        self.tblRegistrado.setShowGrid(True)
        self.tblRegistrado.setColumnCount(3)
        self.tblRegistrado.setObjectName("tblRegistrado")
        self.tblRegistrado.setRowCount(0)
        self.cmbDispositivos = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDispositivos.setGeometry(QtCore.QRect(180, 28, 181, 22))
        self.cmbDispositivos.setObjectName("cmbDispositivos")
        self.txtConsumoWH = QtWidgets.QLineEdit(self.centralwidget)
        self.txtConsumoWH.setGeometry(QtCore.QRect(180, 88, 91, 21))
        self.txtConsumoWH.setObjectName("txtConsumoWH")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(280, 70, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setObjectName("btnAgregar")
        self.lblAreas_5 = QtWidgets.QLabel(self.centralwidget)
        self.lblAreas_5.setGeometry(QtCore.QRect(30, 360, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAreas_5.setFont(font)
        self.lblAreas_5.setObjectName("lblAreas_5")
        self.txtTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(120, 360, 131, 20))
        self.txtTotal.setObjectName("txtTotal")
        self.btnProcesar = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcesar.setGeometry(QtCore.QRect(280, 350, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnProcesar.setFont(font)
        self.btnProcesar.setObjectName("btnProcesar")
        frmConsumo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmConsumo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        frmConsumo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmConsumo)
        self.statusbar.setObjectName("statusbar")
        frmConsumo.setStatusBar(self.statusbar)

        self.retranslateUi(frmConsumo)
        QtCore.QMetaObject.connectSlotsByName(frmConsumo)

    def retranslateUi(self, frmConsumo):
        _translate = QtCore.QCoreApplication.translate
        frmConsumo.setWindowTitle(_translate("frmConsumo", "Administración de Consumo"))
        self.lblAreas.setText(_translate("frmConsumo", "Areas"))
        self.lblAreas_2.setText(_translate("frmConsumo", "Consumos Registrados"))
        self.lblDispo.setText(_translate("frmConsumo", "Dispositivos"))
        self.lblConsumoWh.setText(_translate("frmConsumo", "Consumo (W/h"))
        self.btnAgregar.setText(_translate("frmConsumo", "Agregar"))
        self.lblAreas_5.setText(_translate("frmConsumo", "Consumo Total"))
        self.btnProcesar.setText(_translate("frmConsumo", "Procesar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConsumo = QtWidgets.QMainWindow()
    ui = Ui_frmConsumo()
    ui.setupUi(frmConsumo)
    frmConsumo.show()
    sys.exit(app.exec_())
