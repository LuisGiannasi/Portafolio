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
        frmCarga.resize(543, 474)
        self.centralwidget = QtWidgets.QWidget(frmCarga)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_3.setObjectName("label_3")
        self.cmbTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cmbTipo.setGeometry(QtCore.QRect(150, 60, 231, 22))
        self.cmbTipo.setObjectName("cmbTipo")
        self.spnDias = QtWidgets.QSpinBox(self.centralwidget)
        self.spnDias.setGeometry(QtCore.QRect(150, 100, 61, 22))
        self.spnDias.setMaximum(99)
        self.spnDias.setObjectName("spnDias")
        self.chkSinHaberes = QtWidgets.QCheckBox(self.centralwidget)
        self.chkSinHaberes.setGeometry(QtCore.QRect(250, 100, 131, 17))
        self.chkSinHaberes.setObjectName("chkSinHaberes")
        self.txtRegistros = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtRegistros.setGeometry(QtCore.QRect(30, 200, 481, 231))
        self.txtRegistros.setObjectName("txtRegistros")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.btnGrabar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGrabar.setGeometry(QtCore.QRect(420, 20, 91, 31))
        self.btnGrabar.setObjectName("btnGrabar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(420, 80, 91, 31))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(420, 140, 91, 31))
        self.btnSalir.setObjectName("btnSalir")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_5.setObjectName("label_5")
        self.datFecha = QtWidgets.QDateEdit(self.centralwidget)
        self.datFecha.setGeometry(QtCore.QRect(160, 140, 110, 22))
        self.datFecha.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 28), QtCore.QTime(0, 0, 0)))
        self.datFecha.setMinimumDate(QtCore.QDate(2021, 6, 28))
        self.datFecha.setCalendarPopup(True)
        self.datFecha.setObjectName("datFecha")
        self.spnLegajo = QtWidgets.QSpinBox(self.centralwidget)
        self.spnLegajo.setGeometry(QtCore.QRect(150, 20, 131, 22))
        self.spnLegajo.setMinimum(1000)
        self.spnLegajo.setMaximum(1021)
        self.spnLegajo.setObjectName("spnLegajo")
        frmCarga.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmCarga)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        frmCarga.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmCarga)
        self.statusbar.setObjectName("statusbar")
        frmCarga.setStatusBar(self.statusbar)

        self.retranslateUi(frmCarga)
        QtCore.QMetaObject.connectSlotsByName(frmCarga)

    def retranslateUi(self, frmCarga):
        _translate = QtCore.QCoreApplication.translate
        frmCarga.setWindowTitle(_translate("frmCarga", "Licencias"))
        self.label.setText(_translate("frmCarga", "Legajo Empleado"))
        self.label_2.setText(_translate("frmCarga", "Tipo de Licencia"))
        self.label_3.setText(_translate("frmCarga", "Cantidad de Días"))
        self.chkSinHaberes.setText(_translate("frmCarga", "Sin Cobro de Haberes"))
        self.label_4.setText(_translate("frmCarga", "Registros"))
        self.btnGrabar.setText(_translate("frmCarga", "Grabar"))
        self.btnConsultar.setText(_translate("frmCarga", "&Consultar"))
        self.btnSalir.setText(_translate("frmCarga", "&Salir"))
        self.label_5.setText(_translate("frmCarga", "Fecha Inicial"))
        self.datFecha.setDisplayFormat(_translate("frmCarga", "dd/MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCarga = QtWidgets.QMainWindow()
    ui = Ui_frmCarga()
    ui.setupUi(frmCarga)
    frmCarga.show()
    sys.exit(app.exec_())

