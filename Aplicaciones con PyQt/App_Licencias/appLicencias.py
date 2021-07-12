#importar los archivos python a usar
from PyQt5 import QtWidgets
from frmCarga import *
from frmConsulta import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import datetime

##############################################################################
#clase para construir el formulario de consulta de datos
class appConsulta(QtWidgets.QDialog, Ui_frmConsulta):
    
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # inicialización de componentes
        self.cmbTipo.clear()
        self.cmbTipo.addItem('Vacaciones')
        self.cmbTipo.addItem('Enfermedad')
        self.cmbTipo.addItem('Estudio')   
        self.cmbTipo.addItem('Maternidad')

        # eventos
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnSalir.clicked.connect(self.salir)

        # conexión con la base de datos (implementar)
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn1') #establece le tipo de base y el nombre de la conexión
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\\PROGRAM_II\\Practica_Clase_9\\IEFI_Programacion2-Giannasi\\RRHH.db") # ubicación y nombre del archivo físico de la base de datos
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en base de datos.\n\n", QMessageBox.Cancel)
        else:
            pass
        
        if self.cnn.isOpen():        
            # cargar columnas en la Tabla
            self.modeloLicencias = QSqlTableModel(None, self.cnn)
            self.modeloLicencias.setTable("Licencias")
            self.modeloLicencias.setEditStrategy(QSqlTableModel. OnFieldChange)
            self.modeloLicencias.setHeaderData(0, Qt.Horizontal, "Legajo") #nombres de campos
            self.modeloLicencias.setHeaderData(1, Qt.Horizontal, "TipoLicencia") 
            self.modeloLicencias.setHeaderData(2, Qt.Horizontal, "Dias")
            self.modeloLicencias.setHeaderData(3, Qt.Horizontal, "CobraHaberes")
            self.modeloLicencias.setHeaderData(4, Qt.Horizontal, "FechaInicio")
            
            self.modeloLicencias.select()
            self.tblLicencias.setModel(self.modeloLicencias)
            self.tblLicencias.show()

    def consultar(self):
        self.modeloLicencias.setFilter("TipoLicencia = '{}' ".format(self.cmbTipo.currentText()))
        pass # implementar la consulta de datos en la tabla Licencias

    def salir(self):
        if self.cnn.isOpen():
            self.cnn.close() # cerrar la conexión con la base
            del self.cnn # borra el objeto cnn
            QSqlDatabase.removeDatabase('cnn') # liberar los recursos 
        self.close()
        pass # implementar el cierre de la conexión con la base de datos


##############################################################################
#clase principal de la aplicación, hereda de frmCarga
class appLicencias(QtWidgets.QMainWindow, Ui_frmCarga):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #agregar acá la inicialización del los componentes de la interfaz gráfica
        self.cmbTipo.clear()
        self.cmbTipo.addItem('Vacaciones')
        self.cmbTipo.addItem('Enfermedad')
        self.cmbTipo.addItem('Estudio')   
        self.cmbTipo.addItem('Maternidad')
        self.spnDias.setMinimum(1)
        self.spnDias.setMaximum(180)

        # eventos de los botones
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnSalir.clicked.connect(self.salir)

        #conexion con la base de datos
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn2') #establece le tipo de base y el nombre de la conexión
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\\PROGRAM_II\\Practica_Clase_9\\IEFI_Programacion2-Giannasi\\RRHH.db") # ubicación y nombre del archivo físico de la base de datos
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en base de datos.\n\n", QMessageBox.Cancel)
        else:
            pass

    def grabar(self):
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en base de datos.\n\n", QMessageBox.Cancel)
        else:
        # implemetar la carga de datos en la tabla Licencias
            legajo = str(self.spnLegajo.value())
            licencia = str(self.cmbTipo.currentText())
            dias = str(self.spnDias.value())
            cobro = str(self.chkSinHaberes.isChecked())
            fecha = self.datFecha.dateTime().toString("dd MMM yyyy")
            self.txtRegistros.setPlainText(self.txtRegistros.toPlainText() + "{} - {} - {} - {} - {} \n".format(legajo.strip(), licencia.strip(), dias.strip(), cobro.strip(), fecha.strip()))
    
        #Cargar datos en la base de datos
        cursor = QSqlQuery(self.cnn)
        cursor.exec_("insert into Licencias values("+legajo+",'"+licencia+"',"+dias+","+cobro+",'"+fecha+"')")

    def consultar(self): # crea y visualiza el formulario de consulta de datos
        f2 = appConsulta(self)
        f2.show()

    def salir(self):
        if self.cnn.isOpen():
            self.cnn.close() # cerrar la conexión con la base
            del self.cnn # borra el objeto cnn
            QSqlDatabase.removeDatabase('cnn') # liberar los recursos 
        self.close()

if __name__ == "__main__":   #inicio de la aplicación
    app = QtWidgets.QApplication([])
    window = appLicencias()
    window.show()
    app.exec_()