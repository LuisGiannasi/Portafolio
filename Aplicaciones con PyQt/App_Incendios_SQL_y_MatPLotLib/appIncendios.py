#importar los archivos python a usar
from frmIncendios import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import QDate, QDateTime
from PyQt5 import QtCore, QtWidgets

# módulos de matplotlib vinculados a Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# imports para cálculos y funciones
import numpy as np

##############################################################################
#clase principal de la aplicación, hereda de Ui_frmWeb
class appIncendios(QtWidgets.QMainWindow, Ui_frmIncendios):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # construcción del gráfico
        layout = QtWidgets.QVBoxLayout(self.widget)  #se crea un layout vertical a partir del widget de la interfaz
        self.plot_canvas = FigureCanvas(Figure(figsize=(5, 2))) # se crea el canvas (lienzo de dibujo) epecificando el tamaño en ancho y alto (5,3)
        layout.addWidget(self.plot_canvas) # se agrega al layout el canvas construido
        self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plot_canvas, self)) # se agrega al mismo layout la toolbar provista por la librería de matplot
        self.axes = self.plot_canvas.figure.subplots()
        
        #agregar acá la inicialización del los componentes de la interfaz heredada
        self.cmbProvincias.currentIndexChanged.connect(self.graficar_barras)
        self.chkGraficar.clicked.connect(self.graficar_barras)

        #conexion con la base de datos
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn1')
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\\PROGRAM_II\\Practica_Clase_9\\EjercicioParcial\\Incendios.db") # nombre del archivo físico
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en open baseModelo.\n\n", QMessageBox.Cancel)
        else:
            QMessageBox.information(None, "Conectado", "Conexión exitosa a baseModelo.\n\n", QMessageBox.Ok)

        if self.cnn.isOpen():        
            #leer la tabla Pronostico
            self.modeloIncendios = QSqlTableModel(None, self.cnn)
            self.modeloIncendios.setTable("incendios_provincia")
            self.modeloIncendios.setEditStrategy(QSqlTableModel. OnFieldChange)
            self.modeloIncendios.setHeaderData(0, Qt.Horizontal, "incendio_anio") #nombres de campos
            self.modeloIncendios.setHeaderData(1, Qt.Horizontal, "incendio_provincia") 
            self.modeloIncendios.setHeaderData(2, Qt.Horizontal, "incendio_total_numero")
            self.modeloIncendios.setHeaderData(3, Qt.Horizontal, "incendio_internacional_numero")
            self.modeloIncendios.setHeaderData(4, Qt.Horizontal, "incendio_natural_numero")
            self.modeloIncendios.setHeaderData(5, Qt.Horizontal, "incendio_desconocido_numero")
            self.modeloIncendios.select()
            
            self.tblIncendiosProvincias.setModel(self.modeloIncendios)
            self.tblIncendiosProvincias.show()
        else:
            QMessageBox.critical(None, "Error", "Error en conexión con la base de datos.\n\n", QMessageBox.Cancel)

        #Cargar la lista con provincias
        cursor = QSqlQuery(self.cnn)
        cursor.exec_("SELECT DISTINCT incendio_provincia FROM incendios_provincia")
        self.cmbProvincias.clear()
        while cursor.next():
            self.cmbProvincias.addItem(cursor.value(0))

    def graficar_barras(self):  
        self.axes.cla() # limpia el grafico anterior
        cursor = QSqlQuery(self.cnn)
        cursor.exec_("SELECT * FROM incendios_provincia WHERE incendio_provincia = '"+self.cmbProvincias.currentText( )+"' group by incendio_anio")
        
        if not self.chkGraficar.isChecked():
            valores_x = []
            valores_y = []

            while cursor.next():
                valores_x.append(cursor.value(0))
                valores_y.append(cursor.value(2))
            
            self.axes.bar(valores_x, valores_y) # dibuja la linea de puntos de color green (serían las temp mínimas)
        else:
            valores_x = []
            valores_y1 = []
            valores_y2 = []
            valores_y3 = []
            valores_y4 = []

            while cursor.next():
                valores_x.append(cursor.value(0))
                valores_y1.append(cursor.value(3))
                valores_y2.append(cursor.value(4))
                valores_y3.append(cursor.value(5))
                valores_y4.append(cursor.value(6))

            self.axes.bar(valores_x, np.array(valores_y1), label = "Negligencia") 
            self.axes.bar(valores_x, np.array(valores_y2), bottom = np.array(valores_y1), label = "Intencional")
            self.axes.bar(valores_x, np.array(valores_y3), bottom = np.array(valores_y1) + np.array(valores_y2), label = "Natural")
            self.axes.bar(valores_x, np.array(valores_y4), bottom = np.array(valores_y1) + np.array(valores_y2) + np.array(valores_y3), label = "Desconocido")

        self.plot_canvas.draw() # actualiza el dibujo del grafico
            
if __name__ == "__main__":   #inicio de la aplicación
    app = QtWidgets.QApplication([])
    window = appIncendios()
    window.show()
    app.exec_()