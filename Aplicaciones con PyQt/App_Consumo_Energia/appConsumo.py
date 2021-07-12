#template para trabajar con una ventana de tipo MainWindow

from typing import get_args
from frmConsumo import *  #nombre del archivo convertido con pyuic5 (sin la extensión .py)
from PyQt5  import *


class appConsumo(QtWidgets.QMainWindow, Ui_frmConsumo):

    #Areas: 'Producción', 'Mantenimiento', 'Servicio'
    
    # datos de dispositivos por área
    DP = ['Torno CNC', 'Horno Secado', 'Compresor 80L'] # de Producción
    DM = ['Taladro Percutor', 'Amoladora 115mm', 'Lijadora Orbital'] # de Mantenimiento
    DS = ['Impresora Laser', 'Fotocopiadora Color', 'Dispenser'] # de Servicio

# Constructor de la clase
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

     #Cargar la lista   
        self.lstAreas.clear()
        self.lstAreas.addItem('Producciòn')
        self.lstAreas.addItem('Mantenimiento')
        self.lstAreas.addItem('Servicio')

        self.txtConsumoWH.setText("")
        self.txtTotal.setText("")

        self.lstAreas.itemClicked.connect(self.CargaDispositvos)
        self.btnAgregar.clicked.connect(self.AgregarConsumo)
        self.btnProcesar.clicked.connect(self.ProcesarTotales)

        #Encabezado de tablas
        header = QtWidgets.QTableWidgetItem('Area')
        self.tblRegistrado.setHorizontalHeaderItem(0, header)
        header = QtWidgets.QTableWidgetItem('Dispositivo')
        self.tblRegistrado.setHorizontalHeaderItem(1, header)
        header = QtWidgets.QTableWidgetItem('Consumo (W/h)')
        self.tblRegistrado.setHorizontalHeaderItem(2, header)


    def CargaDispositvos(self):
        item = self.lstAreas.currentRow()
        self.cmbDispositivos.clear()
        
        if item == 0:
            for d in self.DP:
                self.cmbDispositivos.addItem(d)

        if item == 1:
            for d in self.DM:
                self.cmbDispositivos.addItem(d)

        if item == 2:
            for d in self.DS:
                self.cmbDispositivos.addItem(d)

    def AgregarConsumo(self):
        row = self.tblRegistrado.rowCount()
        self.tblRegistrado.insertRow(row)
        area = QtWidgets.QTableWidgetItem(self.lstAreas.currentItem().text())
        self.tblRegistrado.setItem( row, 0, area)
        dispositivo = QtWidgets.QTableWidgetItem(self.cmbDispositivos.currentText())
        self.tblRegistrado.setItem( row, 1, dispositivo)
        consumo = QtWidgets.QTableWidgetItem(self.txtConsumoWH.text())
        print(consumo)
        self.tblRegistrado.setItem( row, 2, consumo)
        return consumo

    def ProcesarTotales(self):
        rowCount = self.tblRegistrado.rowCount()
        totalConsumo = 0
        for row in range(0, rowCount):
            item = self.tblRegistrado.item(row, 2)
            consumo = float(item.text())
            totalConsumo += consumo
        self.txtTotal.setText(str(totalConsumo))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = appConsumo()
    window.show()
    app.exec_()
    
