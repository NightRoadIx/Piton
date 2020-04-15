import sys
from PyQt5 import uic, QtWidgets

# Archivo con la vista
qtCreatorFile = "polinomio.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.calculos)
        
    def calculos(self):
        import numpy as np
        P = np.zeros([3])
        P[0] = float( self.cuadratico.toPlainText() )
        P[1] = float( self.lineal.toPlainText() )
        P[2] = float( self.independiente.toPlainText() )
        raiz_st = "Su resultado es: " + str( np.roots(P) )
        self.raiz.setText(raiz_st)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())