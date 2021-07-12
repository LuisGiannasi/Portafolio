#template para trabajar con una ventana de tipo MainWindow

from PyQt5 import QtWidgets
from frmEncuesta import *  #nombre del archivo convertido con pyuic5 (sin la extensión .py)

class appEncuesta(QtWidgets.QMainWindow, Ui_frmEncuesta):

    # TIPO = [“Utilitario”, “Automóvil Familiar”, “Automóvil Deportivo” y “Motocicleta”.]

# Constructor de la clase
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #Cargar la lista con Aceites
        self.cmbVehiculo.clear()
        self.cmbVehiculo.addItem('Utilitario')
        self.cmbVehiculo.addItem('Automóvil Familiar')
        self.cmbVehiculo.addItem('Automóvil Deportivo')   
        self.cmbVehiculo.addItem('Motocicleta')

        #Estado inicial
        header = QtWidgets.QTableWidgetItem("Tipo")
        self.tblEncuesta.setHorizontalHeaderItem(0,header)
        header = QtWidgets.QTableWidgetItem("Dias")
        self.tblEncuesta.setHorizontalHeaderItem(1,header)
        header = QtWidgets.QTableWidgetItem("Kmts")
        self.tblEncuesta.setHorizontalHeaderItem(2,header)
        header = QtWidgets.QTableWidgetItem("Calificación")
        self.tblEncuesta.setHorizontalHeaderItem(3,header)
        header = QtWidgets.QTableWidgetItem("Evaluación")
        self.tblEncuesta.setHorizontalHeaderItem(4,header)

        #Fijar ancho de columnas
        self.tblEncuesta.setColumnWidth(0,120)
        self.tblEncuesta.setColumnWidth(1,40)
        self.tblEncuesta.setColumnWidth(2,80)
        self.tblEncuesta.setColumnWidth(3,90)
        self.tblEncuesta.setColumnWidth(4,90)

        self.pbrEncuesta.setValue(0)

        #Establecer Propiedades
        self.optMB.setChecked(True)
        self.btnEvaluar.setEnabled(False)
        self.btnRegistrar.setEnabled(False)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnRestablecer.clicked.connect(self.restablecer)
        self.btnEvaluar.clicked.connect(self.evaluar)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.leKm.textChanged.connect(self.actualizarEstado)

        
        self.acum = []

    def actualizarEstado(self):
        if len(self.leKm.text()) > 0:
            self.btnRegistrar.setEnabled(True)
        else:
            self.btnRegistrar.setEnabled(False)

        #agregar otros metodos
    def registrar(self):
        aux = 0
        
        if self.optMB.isChecked():
            aux += (int(self.leKm.text()) / self.spbDias.value()) * 0.95  
        if self.optB.isChecked():
            aux += (int(self.leKm.text()) / self.spbDias.value()) * 0.7
        if self.optR.isChecked():
            aux += (int(self.leKm.text()) / self.spbDias.value()) * 0.5
        if self.optM.isChecked():
            aux += (int(self.leKm.text()) / self.spbDias.value()) * 0.2
        
        if self.optMB.isChecked():
            cali = "Muy Bueno"  
        if self.optB.isChecked():
            cali = "Bueno"
        if self.optR.isChecked():
            cali = "Regular"
        if self.optM.isChecked():
            cali = "Malo"

        self.lePromedio.setText("{0:.2f}".format(aux))

        #Cargar la Tabla
        row = self.tblEncuesta.rowCount()
        self.tblEncuesta.setRowCount(row+1)
        tipo = QtWidgets.QTableWidgetItem(self.cmbVehiculo.currentText())
        self.tblEncuesta.setItem(row, 0, tipo)    
        dias = QtWidgets.QTableWidgetItem(str(self.spbDias.value()))
        self.tblEncuesta.setItem(row, 1, dias) 
        kmts = QtWidgets.QTableWidgetItem(str(self.leKm.text()))
        self.tblEncuesta.setItem(row, 2, kmts) 
        calif = QtWidgets.QTableWidgetItem(cali)
        self.tblEncuesta.setItem(row, 3, calif) 
        eval = QtWidgets.QTableWidgetItem(str(self.lePromedio.text()))
        self.tblEncuesta.setItem(row, 4, eval) 

        progreso = self.pbrEncuesta.value()
        self.pbrEncuesta.setValue(progreso+20)
        if self.pbrEncuesta.value() == 100:
            self.btnEvaluar.setEnabled(True)


        self.leKm.setText("")
        self.spbDias.setValue(0)
        self.optMB.isChecked()
        self.optB.isChecked()
        self.optR.isChecked()
        self.optM.isChecked()
        self.cmbVehiculo.clear()
        self.cmbVehiculo.addItem('Utilitario')
        self.cmbVehiculo.addItem('Automóvil Familiar')
        self.cmbVehiculo.addItem('Automóvil Deportivo')   
        self.cmbVehiculo.addItem('Motocicleta')
        self.optMB.setChecked(True)
        self.optB.setChecked(False)
        self.optR.setChecked(False)
        self.optM.setChecked(False)

        self.acum.append(aux)

    def restablecer(self):
        self.cmbVehiculo.clear()
        self.cmbVehiculo.addItem('Utilitario')
        self.cmbVehiculo.addItem('Automóvil Familiar')
        self.cmbVehiculo.addItem('Automóvil Deportivo')  
        self.cmbVehiculo.addItem('Motocicleta')  
        self.spbDias.setValue(0)
        self.lePromedio.setText("")
        self.leKm.setText("")
        self.optMB.setChecked(True)
        self.optB.setChecked(False)
        self.optR.setChecked(False)
        self.optM.setChecked(False)
        self.pbrEncuesta.setValue(0)
        self.tblEncuesta.setRowCount(0)
        self.lePromedio_2.setText("")
        self.btnRegistrar.setEnabled(True)

    def evaluar(self):
        try:
            total = 0 
            for i in range(0, self.tblEncuesta.rowCount()):
                total += float(self.tblEncuesta.item(i, 4).text())

            promedio = total/ self.tblEncuesta.rowCount()
            self.lePromedio_2.setText("{0:.2f}".format(promedio))
            self.statusBar().showMessage('Promedio calculado sobre {} evaluaciones'.format(self.tblEncuesta.rowCount()))
            self.btnEvaluar.setEnabled(False)
            self.btnRegistrar.setEnabled(False)
        except:
            self.statusBar().showMessage('No se pudo calcular el promedio')
            self.btnEvaluar.setEnabled(False)       

    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = appEncuesta()
    window.show()
    app.exec_()