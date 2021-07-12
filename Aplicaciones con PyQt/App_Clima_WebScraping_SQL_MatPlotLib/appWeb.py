#importar los archivos python a usar
from PyQt5 import QtWidgets
from frmWeb import *

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import QDate, QDateTime
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

# módulos de matplotlib vinculados a Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

fecha = QDate.currentDate().toPyDate()

##############################################################################
#clase principal de la aplicación, hereda de Ui_frmWeb
class appWeb(QtWidgets.QMainWindow, Ui_frmWeb):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #agregar acá la inicialización del los componentes de la interfaz heredada
        self.btnCargar.clicked.connect(self.cargarPronostico)
        self.btnCargar.clicked.connect(self.grabar)
        # self.cmbFecha.currentIndexChanged.connect(self.graficar)
        self.btnConsultar.clicked.connect(self.graficar)

        # construcción del gráfico
        layout = QtWidgets.QVBoxLayout(self.widget)  #se crea un layout vertical a partir del widget de la interfaz
        self.plot_canvas = FigureCanvas(Figure(figsize=(5, 2))) # se crea el canvas (lienzo de dibujo) epecificando el tamaño en ancho y alto (5,3)
        layout.addWidget(self.plot_canvas) # se agrega al layout el canvas construido
        self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.plot_canvas, self)) # se agrega al mismo layout la toolbar provista por la librería de matplot
        self.axes = self.plot_canvas.figure.subplots()

        #conexion con la base de datos
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn1')
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\PROGRAM_II\\Practica_Clase_9\\TP_PROGRAM_II_Giannasi\\Clima.db") # nombre del archivo físico
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en open baseModelo.\n\n", QMessageBox.Cancel)
        else:
            #pass
            QMessageBox.information(None, "Conectado", "Conexión exitosa a baseModelo.\n\n", QMessageBox.Ok)
        self.cargar_combo()

        if self.cnn.isOpen():        
            #leer la tabla Pronostico
            self.modeloClima = QSqlTableModel(None, self.cnn)
            self.modeloClima.setTable("Pronostico")
            self.modeloClima.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.modeloClima.setHeaderData(0, Qt.Horizontal, "FechaReg") #nombres de campos
            self.modeloClima.setHeaderData(1, Qt.Horizontal, "FechaPron") 
            self.modeloClima.setHeaderData(2, Qt.Horizontal, "EstActual")
            self.modeloClima.setHeaderData(3, Qt.Horizontal, "TempMin")
            self.modeloClima.setHeaderData(4, Qt.Horizontal, "TempMax")
            self.modeloClima.select()
            self.tblClima.setModel(self.modeloClima)
            self.tblClima.show()
        else:
            QMessageBox.critical(None, "Error", "Error en conexión con la base de datos.\n\n", QMessageBox.Cancel)

    def buscar_fecha(self, rec_param):
        cant_reg = self.modeloClima.rowCount()
        for i in range(cant_reg):
            rec = self.modeloClima.record(i)
            if rec.value('FechaReg') == rec_param.value('FechaReg') and rec.value('FechaPron') == rec_param.value('FechaPron'):
                self.modeloClima.removeRows(i, 1)
                return i
        return cant_reg
                   
    def grabar(self):
        if self.modeloClima.isDirty():
            self.modeloClima.submitAll()
            self.modeloClima.select()
            self.cargar_combo()

    def cargarPronostico(self):
        #cargar el browser con la página a explorar
        url = QUrl()
        url.setUrl("https://infoclima.com/pronosticos/argentina/cordoba/cordoba/extendido/")
        self.browser.setUrl(url)

        # obtener el contenido de la página
        page = urllib.request.urlopen('https://infoclima.com/pronosticos/argentina/cordoba/cordoba/extendido/').read()
        #crear el objeto con el parser HTML
        soup = BeautifulSoup(page, 'html.parser')
        #leer de la página la clase "nota1 prE" que contiene todos los elementos del prónostico por 7 días
        semana = soup.find(class_="nota1 prE")
        semana_items = semana.findAll(class_="row") # leer todos los items con clase "row"
        for item in semana_items: # recorrer todos los items 
            if item.find(class_="col-md-2 d"): 
                #leer el texto contenido en cada item
                diaReg = datetime.today().strftime('%y-%m-%d').strip() #setea la fecha de la busqueda de los datos
                diaPron = item.find(class_="col-md-2 d").get_text().strip() # leer la fecha
                actual = item.find(class_="col-md-2 col-xs-4 i").get_text().strip() #leer el estado actual
                tempMin = item.find(class_="max").get_text().strip() # leer temp min.
                tempMax = item.find(class_="min").get_text().strip() # leer temp máx.
                # se crea un objeto de tipo "record" vacío a partir del modelo
                rec2 = self.modeloClima.record()
                # asignar los valores a cada campo
                rec2.setValue("FechaReg", diaReg)
                rec2.setValue("FechaPron", diaPron)
                rec2.setValue("EstActual", actual)
                rec2.setValue("TMin", float(tempMin.strip('°')))
                rec2.setValue("TMax", float(tempMax.strip('°')))
                
                indice = self.buscar_fecha(rec2)
                self.modeloClima.insertRecord(indice, rec2);
                # la grabación definitiva sobre la base se realiza con el botón "Grabar" (al ejecutar submitAll())

    def cargar_combo(self):
        #Cargar la lista con fechas
        cursor = QSqlQuery(self.cnn)
        cursor.exec_("SELECT DISTINCT FechaReg FROM Pronostico")
        self.cmbFecha.clear()
        while cursor.next():
            self.cmbFecha.addItem(cursor.value(0))

    def graficar(self):  
        self.axes.cla() # limpia el grafico anterior
        cursor = QSqlQuery(self.cnn)
        cursor.exec_("SELECT FechaPron, TMin, TMax FROM Pronostico WHERE FechaReg == '"+self.cmbFecha.currentText()+"'")
        
        valores_x = []
        valores_y1 = []
        valores_y2 = []

        while cursor.next():
            valores_x.append(cursor.value(0))
            valores_y1.append(cursor.value(1))
            valores_y2.append(cursor.value(2))

        self.axes.plot(valores_x, valores_y1, 'g') # dibuja la linea de puntos de color green (serían las temp mínimas)
        self.axes.plot(valores_x, valores_y2, 'r')

        self.plot_canvas.draw() # actualiza el dibujo del grafico

if __name__ == "__main__":   #inicio de la aplicación
    app = QtWidgets.QApplication([])
    window = appWeb()
    window.show()
    app.exec_()