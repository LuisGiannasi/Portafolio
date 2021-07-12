#importar los archivos python a usar
from PyQt5 import QtWidgets
from frmMenu import *
from frmCarga import *
from frmConsulta import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import datetime


##############################################################################
#clase para construir el formulario de carga de datos
class appCarga(QtWidgets.QDialog, Ui_frmCarga):
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # configuracion inicial
        self.txtNumero.setText("")
        self.txtNombre.setText("")
        self.spnClase.setMaximum(int(datetime.datetime.now().year)) #obtiene el año actual

        # eventos de los botones
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCerrar.clicked.connect(self.cerrar)

        #conexion con la base de datos
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn1') #establece le tipo de base y el nombre de la conexión
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\\PROGRAM_II\\Practica_Clase_7\\baseModelo.db") # ubicación y nombre del archivo físico de la base de datos
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en open baseModelo.\n\n", QMessageBox.Cancel)
        else:
            pass
            #QMessageBox.information(None, "Conectado", "Conexión exitosa a baseModelo.\n\n", QMessageBox.Ok)

    def aceptar(self):
        #validar datos
        if len(self.txtNumero.text().strip()) > 0 and len(self.txtNombre.text().strip()) > 0: 
            try:
                numero = int(self.txtNumero.text())
                nombre = self.txtNombre.text()
                clase = int(self.spnClase.value())
                if self.cnn.isOpen():
                    # crear el objeto SqlQuery
                    query = QSqlQuery(None, self.cnn)
                    # sentencia sql dinámica
                    if query.exec(
                        f"""INSERT INTO Personas (Numero, Nombre, Clase)
                            VALUES ('{numero}', '{nombre}', '{clase}')""" # usa un 'f' string
                    ):
                        QMessageBox.information(None, "Agregado", "Registro de datos exitoso.\n\n", QMessageBox.Ok)
                        self.txtNumero.setText("")
                        self.txtNombre.setText("")
                    else:
                        QMessageBox.critical(None, "Error", "Error en registro de datos {}.\n\n".format(self.cnn.lastError()), QMessageBox.Cancel)
                    query.finish() # libera los recursos
                    del query # borra el objeto query
            except:
                QMessageBox.critical(None, "Error", "Error en registro de datos.\n\n", QMessageBox.Cancel)
        else:
            QMessageBox.critical(None, "Error", "Datos incompletos o erróneos.\n\n", QMessageBox.Cancel)

    def cerrar(self):
        if self.cnn.isOpen():
            self.cnn.close() # cerrar la conexión con la base
            del self.cnn # borra el objeto cnn
            QSqlDatabase.removeDatabase('cnn1') # liberar los recursos 
        self.close()

##############################################################################
#clase para construir el formulario de consulta de datos
class appConsulta(QtWidgets.QDialog, Ui_frmConsulta):
    
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # eventos
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.btnBorrar.clicked.connect(self.borrar)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnAplicarFiltro.clicked.connect(self.aplicarFiltro)
        self.cnn = QSqlDatabase.addDatabase('QSQLITE', 'cnn2')
        self.cnn.setDatabaseName("C:\\Users\\luisg\\Documents\\IA\\PROGRAM_II\\Practica_Clase_7\\baseModelo.db") # nombre del archivo físico
        if not self.cnn.open(): # abrir la conexión
            QMessageBox.critical(None, "Error", "Error en open baseModelo.\n\n", QMessageBox.Cancel)
        else:
            pass
            #QMessageBox.information(None, "Conectado", "Conexión exitosa a baseModelo.\n\n", QMessageBox.Ok)

    def consultar(self):
        if self.cnn.isOpen():        
            #leer la tabla Persona
            self.modeloPersona = QSqlTableModel(None, self.cnn)
            self.modeloPersona.setTable("Persona")
            self.modeloPersona.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.modeloPersona.setHeaderData(0, Qt.Horizontal, "Numero") #nombres de campos
            self.modeloPersona.setHeaderData(1, Qt.Horizontal, "Nombre")
            self.modeloPersona.setHeaderData(2, Qt.Horizontal, "Clase")
            self.modeloPersona.select()
            #
            self.tblPersonas.setModel(self.modeloPersona)
            self.tblPersonas.show() # no siempre es necesario usarlo
        else:
            QMessageBox.critical(None, "Error", "Error en conexión con la base de datos.\n\n", QMessageBox.Cancel)

    def aplicarFiltro(self):
        self.modeloPersona.setFilter(self.txtFiltro.text())
        self.modeloPersona.select() 

    def agregar(self):
        index = QModelIndex()
        self.modeloPersona.insertRow(self.modeloPersona.rowCount(), index)

    def actualizar(self):
        try:
            self.tblPersonas.model().submitAll() # escribe todos los cambios en la base 
        except:
            print("Error")
            QMessageBox.critical(None, "Error", "No hay datos para actualizar.\n\n", QMessageBox.Cancel)

        

    def borrar(self):
        index = self.tblPersonas.currentIndex() # obtener el objeto seleccionado en la tabla
        if not index is None and index.row() >= 0:
            deleteconfirmation = QMessageBox.critical(None, "Borrar", "Realmente desea borrar el registro seleccionado?", QMessageBox.Yes, QMessageBox.No)
            if deleteconfirmation == QMessageBox.Yes:
                self.tblPersonas.model().removeRow(index.row()) # se usa el núemero de fila (row) para ubicar el registro a borrar
                self.tblPersonas.model().submitAll()   # se escriben los cambios en la base
        else:
            QMessageBox.information(None, "Borrar", "No hay ningún registro seleccionado para borrar.\n\n", QMessageBox.Ok)

    def cerrar(self):
        if self.cnn.isOpen():
            if self.tblPersonas.model():
                self.tblPersonas.setModel(None)
                del self.modeloPersona
            self.cnn.close() # cerrar la conexión con la base
            del self.cnn
            QSqlDatabase.removeDatabase('cnn2') # liberar los recursos 
        self.close()


##############################################################################
#clase principal de la aplicación, hereda los 2 formlarios anteriores
class appMenu(QtWidgets.QMainWindow, Ui_frmMenu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #agregar acá la inicialización del los componentes de la interfaz heredada
        self.actionCarga_de_Datos.triggered.connect(self.cargar)
        self.actionConsulta_de_Datos.triggered.connect(self.consultar)
        self.actionSalir.triggered.connect(self.salir)


    def cargar(self):
        f1 = appCarga(self) # crea y visuaiza el formulario de carga de datos
        f1.show()
        

    def consultar(self): # crea y visualiza el formulario de consulta de datos
        f2 = appConsulta(self)
        f2.show()

    def salir(self):
        self.close()

if __name__ == "__main__":   #inicio de la aplicación
    app = QtWidgets.QApplication([])
    window = appMenu()
    window.show()
    app.exec_()