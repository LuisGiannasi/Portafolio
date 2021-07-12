# Importar el archivo Python generado de QtDesigner, reemplazar <clase_ui> or el nombre correcto
from form_covid4 import *

# Clase nueva para constuir el dialogo
# Reemplazar <nombreClase> por el nombre adecuado a la funcionalidad e la aplicación
class appCovid4 (QtWidgets.QMainWindow, Ui_frmCovid):
# Constructor de la clase
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        #establecer propiedades
        self.lblProbabilidad.setText("")
        self.optF.setChecked(True)
        self.optMenor.setChecked(True)

        #Valores de Rango
        self.spbCansancio.setMinimum(20.00)    
        self.spbCansancio.setMaximum(40.00)
        self.spbRespirar.setMinimum(7)
        self.spbRespirar.setMaximum(15)
        self.spbCabeza.setMinimum(12.00)  
        self.spbCabeza.setMaximum(27.00)
        self.spbMuscular.setMinimum(2.00)
        self.spbMuscular.setMaximum(6.00)
        self.spbGusto.setMinimum(4)
        self.spbGusto.setMaximum(7)
        self.spbTos.setMinimum(5)
        self.spbTos.setMaximum(10)
        
        self.spbCansancio.setValue(30.00)
        self.spbRespirar.setValue(10)
        self.spbCabeza.setValue(20.00)  
        self.spbMuscular.setValue(4)
        self.spbGusto.setValue(8)
        self.spbTos.setValue(6)
        # self.chkBloquear.setChecked(True)

        #Vicular Eventos y Acciones
        self.btnEvaluar.clicked.connect(self.calcularProbabilidad)
        self.btnRestablecer.clicked.connect(self.restablecer)
        self.btnCerrar.clicked.connect(self.cerrar)
        # self.chkBloquear.clicked.connect(self.bloquear_valores)

    #Agregar otros Metodos
    def bloquear_valores(self):
        if self.chkBloquear.isChecked():
            self.spbCansancio.setEneable(False)
            self.spbRespirar.setEneable(False)
            self.spbCabeza.setEneable(False)  
            self.spbMuscular.setEneable(False)
            self.spbGusto.setEneable(False)
            self.spbTos.setEneable(False)
        else:
            self.spbCansancio.setEneable(True)
            self.spbRespirar.setEneable(True)
            self.spbCabeza.setEneable(True)  
            self.spbMuscular.setEneable(True)
            self.spbGusto.setEneable(True)
            self.spbTos.setEneable(True)

    def calcularProbabilidad(self):
        prob = 0
        if self.chkCansancio.isChecked() == True:
            prob += self.spbCansancio.value()
        if self.chkCabeza.isChecked() == True:
            prob += self.spbCabeza.value()
        if self.chkRespirar.isChecked() == True:
            prob += self.spbRespirar.value()
        if self.chkTos.isChecked() == True:
            prob += self.spbTos.value()
        if self.chkGusto.isChecked() == True:
            prob += self.spbGusto.value()
        if self.chkMuscular.isChecked() == True:
            prob += self.spbMuscular.value()
        
        if self.optM.isChecked():
            prob = prob * 1.05
        if self.optMayor.isChecked():
            prob = prob * 1.1
        
        self.lblProbabilidad.setText(str(prob))

        #Agregar resultados a la lista
        if self.lstResultados.count() == 4:
            self.lstResultados.clear()
        
        self.lstResultados.addItem(str(prob))
    
    def restablecer(self):
        self.chkCansancio.setChecked(False)
        self.chkCabeza.setChecked(False)
        self.chkRespirar.setChecked(False)
        self.chkTos.setChecked(False)
        self.chkGusto.setChecked(False)
        self.chkMuscular.setChecked(False)
        self.optF.setChecked(True)
        self.optMenor.setChecked(True)
        self.lblProbabilidad.setText("")
        self.spbCansancio.setValue(30.00)
        self.spbRespirar.setValue(10)
        self.spbCabeza.setValue(20.00)  
        self.spbMuscular.setValue(4)
        self.spbGusto.setValue(8)
        self.spbTos.setValue(6)
        self.lstResultados.clear()
    
    def cerrar(self):
        self.close()

# Punto de inicio del programa
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = appCovid4() #Reemplazar <nombreClase> por el mismo nombre de clase anteriormente establecido
    window.show()
    app.exec_()