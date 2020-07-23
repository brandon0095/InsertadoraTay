#from Insertadora_ui import *
from MasPeque import *
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import serial

_translate = QtCore.QCoreApplication.translate

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.texCali.setEnabled(not self.TexPW.isEnabled())
        

        # Eventos (1) 
        self.Btn3.clicked.connect(self.btnPalo3)       # PALO 3
        self.Btn4.clicked.connect(self.btnPalo4)       # PALO 4
        self.Btn5.clicked.connect(self.btnPalo5)       # PALO 5
        self.Btn6.clicked.connect(self.btnPalo6)       # PALO 6
        self.Btn7.clicked.connect(self.btnPalo7)       # PALO 7
        self.Btn8.clicked.connect(self.btnPalo8)       # PALO 8
        self.Btn9.clicked.connect(self.btnPalo9)       # PALO 9
        self.BtnPW.clicked.connect(self.btnPaloPW)     # PALO PW
        self.BtnAw.clicked.connect(self.btnPaloAW)     # PALO AW
        self.BtnSW.clicked.connect(self.btnPaloSW)     # PALO SW
        
        # Eventos (2)
        self.BtnCalibrar.clicked.connect(self.updateLong)     # Actualizar longitud
        self.BtnLimpiar.clicked.connect(self.clearResults)    # Limpiar Resultados
        self.BtnEmpezar.clicked.connect(self.disableElements) # Bloquear 
            
    def btnPalo3(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex3.toPlainText():
            return
            
        longitudEsperado = float(self.Tex3.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_3.setText(str("{:.2f}".format(longitudTotal)))    
        self.Diferencia_3.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
    
    def btnPalo4(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex4.toPlainText():
            return
            
        longitudEsperado = float(self.Tex4.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_4.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_4.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))


    def btnPalo5(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex5.toPlainText():
            return
            
        longitudEsperado = float(self.Tex5.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_5.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_5.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
    
    def btnPalo6(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex6.toPlainText():
            return
            
        longitudEsperado = float(self.Tex6.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_6.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_6.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
        
    def btnPalo7(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex7.toPlainText():
            return
            
        longitudEsperado = float(self.Tex7.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))

        self.Lon_7.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_7.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
            
    def btnPalo8(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex8.toPlainText():
            return
            
        longitudEsperado = float(self.Tex8.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))

        self.Lon_8.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_8.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
        
    def btnPalo9(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.Tex9.toPlainText():
            return
            
        longitudEsperado = float(self.Tex9.toPlainText())
        print(longitudTotal-longitudEsperado)

        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_9.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_9.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
        
    def btnPaloPW(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.TexPW.toPlainText():
            return
        
        longitudEsperado = float(self.TexPW.toPlainText())
        print(longitudTotal-longitudEsperado)

        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_PW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_PW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_PW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))

        self.Lon_PW.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_PW.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
        
    def btnPaloAW(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.TexAW.toPlainText():
            return

        longitudEsperado = float(self.TexAW.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_AW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_AW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_AW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
        
        self.Lon_AW.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_AW.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
              
    def btnPaloSW(self):
        longitudTotal = float(self.texCali.toPlainText())
        if not self.TexSW.toPlainText():
            return
        
        longitudEsperado = float(self.TexSW.toPlainText())
        print(longitudTotal-longitudEsperado)
        
        if (longitudTotal-longitudEsperado) < 0.09 and (longitudTotal-longitudEsperado) > -0.09 :
            self.Res_SW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">Correcto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) < 0.10:
            self.Res_SW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffff00;\">Corto</span></p></body></html>"))
        elif (longitudTotal-longitudEsperado) > -0.10:
            self.Res_SW.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Largo</span></p></body></html>"))
            
        self.Lon_SW.setText(str("{:.2f}".format(longitudTotal)))
        self.Diferencia_SW.setText(str("{:.2f}".format(longitudTotal-longitudEsperado)))
            

    def clearResults(self):
           self.Res_3.setText("-")
           self.Res_4.setText("-")
           self.Res_5.setText("-")
           self.Res_6.setText("-")
           self.Res_7.setText("-")
           self.Res_8.setText("-")
           self.Res_9.setText("-")
           self.Res_PW.setText("-")
           self.Res_AW.setText("-")
           self.Res_RS.setText("-")
           
           self.Lon_3.setText("-")
           self.Lon_4.setText("-")
           self.Lon_5.setText("-")
           self.Lon_6.setText("-")
           self.Lon_7.setText("-")
           self.Lon_8.setText("-")
           self.Lon_9.setText("-")
           self.Lon_PW.setText("-")
           self.Lon_AW.setText("-")
           self.Lon_SW.setText("-")
           
           self.Diferencia_3.setText("-")
           self.Diferencia_4.setText("-")
           self.Diferencia_5.setText("-")
           self.Diferencia_6.setText("-")
           self.Diferencia_7.setText("-")
           self.Diferencia_8.setText("-")
           self.Diferencia_9.setText("-")
           self.Diferencia_PW.setText("-")
           self.Diferencia_AW.setText("-")
           self.Diferencia_SW.setText("-")
           
    def disableElements(self):
        self.Tex3.setEnabled(not self.Tex3.isEnabled())
        self.Tex4.setEnabled(not self.Tex4.isEnabled())
        self.Tex5.setEnabled(not self.Tex5.isEnabled())  
        self.Tex6.setEnabled(not self.Tex6.isEnabled())
        self.Tex7.setEnabled(not self.Tex7.isEnabled())
        self.Tex8.setEnabled(not self.Tex8.isEnabled())
        self.Tex9.setEnabled(not self.Tex9.isEnabled())
        self.TexPW.setEnabled(not self.TexPW.isEnabled())
        self.TexAW.setEnabled(not self.TexAW.isEnabled())
        self.TexSW.setEnabled(not self.TexSW.isEnabled())

    def printLong(self, value):
        self.texCali.setText(str(value))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.texCali.setAlignment(QtCore.Qt.AlignCenter)
        self.texCali.setFont(font)
    
    def getLine(self, com):
        if (com == 1):
            ser = serial.Serial('COM4',timeout=0.5)
        elif (com == 2):
            ser = serial.Serial('COM7',timeout=0.5)
        ser.flush()
        ser.write("r")
        line = ser.readline()
        line = line.decode("utf-8")
        return line
    
    def updateLong(self):     
        value1 = self.getLine(1)
        value2 = self.getLine(2)
        totalLong = 51.060 - float(value1) - float(value2)
        self.printLong(totalLong)
                      
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
