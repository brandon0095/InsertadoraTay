# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MasPeque.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1335, 659)
        self.Titulo4 = QtWidgets.QLabel(Dialog)
        self.Titulo4.setGeometry(QtCore.QRect(10, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo4.setFont(font)
        self.Titulo4.setObjectName("Titulo4")
        self.BtnEmpezar = QtWidgets.QPushButton(Dialog)
        self.BtnEmpezar.setGeometry(QtCore.QRect(110, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BtnEmpezar.setFont(font)
        self.BtnEmpezar.setObjectName("BtnEmpezar")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(661, 0, 731, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.Titulo1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo1.setFont(font)
        self.Titulo1.setObjectName("Titulo1")
        self.horizontalLayout_41.addWidget(self.Titulo1)
        self.Titulo2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo2.setFont(font)
        self.Titulo2.setObjectName("Titulo2")
        self.horizontalLayout_41.addWidget(self.Titulo2)
        self.Titulo3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo3.setFont(font)
        self.Titulo3.setObjectName("Titulo3")
        self.horizontalLayout_41.addWidget(self.Titulo3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 50, 381, 521))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.Labt4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt4.setFont(font)
        self.Labt4.setObjectName("Labt4")
        self.horizontalLayout_39.addWidget(self.Labt4)
        self.Tex3 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex3.setObjectName("Tex3")
        self.horizontalLayout_39.addWidget(self.Tex3)
        self.verticalLayout.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.Labt4_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt4_3.setFont(font)
        self.Labt4_3.setObjectName("Labt4_3")
        self.horizontalLayout_37.addWidget(self.Labt4_3)
        self.Tex4 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex4.setObjectName("Tex4")
        self.horizontalLayout_37.addWidget(self.Tex4)
        self.verticalLayout.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Labt5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt5.setFont(font)
        self.Labt5.setObjectName("Labt5")
        self.horizontalLayout_11.addWidget(self.Labt5)
        self.Tex5 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex5.setObjectName("Tex5")
        self.horizontalLayout_11.addWidget(self.Tex5)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Labt6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt6.setFont(font)
        self.Labt6.setObjectName("Labt6")
        self.horizontalLayout_12.addWidget(self.Labt6)
        self.Tex6 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex6.setObjectName("Tex6")
        self.horizontalLayout_12.addWidget(self.Tex6)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Labt7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt7.setFont(font)
        self.Labt7.setObjectName("Labt7")
        self.horizontalLayout_13.addWidget(self.Labt7)
        self.Tex7 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex7.setObjectName("Tex7")
        self.horizontalLayout_13.addWidget(self.Tex7)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Labt8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt8.setFont(font)
        self.Labt8.setObjectName("Labt8")
        self.horizontalLayout_14.addWidget(self.Labt8)
        self.Tex8 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex8.setObjectName("Tex8")
        self.horizontalLayout_14.addWidget(self.Tex8)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.Labt9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Labt9.setFont(font)
        self.Labt9.setObjectName("Labt9")
        self.horizontalLayout_15.addWidget(self.Labt9)
        self.Tex9 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Tex9.setObjectName("Tex9")
        self.horizontalLayout_15.addWidget(self.Tex9)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.LabtPW = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabtPW.setFont(font)
        self.LabtPW.setObjectName("LabtPW")
        self.horizontalLayout_16.addWidget(self.LabtPW)
        self.TexPW = QtWidgets.QTextEdit(self.layoutWidget1)
        self.TexPW.setObjectName("TexPW")
        self.horizontalLayout_16.addWidget(self.TexPW)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.LabtAW = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabtAW.setFont(font)
        self.LabtAW.setObjectName("LabtAW")
        self.horizontalLayout_17.addWidget(self.LabtAW)
        self.TexAW = QtWidgets.QTextEdit(self.layoutWidget1)
        self.TexAW.setObjectName("TexAW")
        self.horizontalLayout_17.addWidget(self.TexAW)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.LabtSW = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabtSW.setFont(font)
        self.LabtSW.setObjectName("LabtSW")
        self.horizontalLayout_18.addWidget(self.LabtSW)
        self.TexSW = QtWidgets.QTextEdit(self.layoutWidget1)
        self.TexSW.setObjectName("TexSW")
        self.horizontalLayout_18.addWidget(self.TexSW)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(401, 46, 931, 521))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.Btn3 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn3.setFont(font)
        self.Btn3.setObjectName("Btn3")
        self.horizontalLayout_40.addWidget(self.Btn3)
        self.Diferencia_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_3.setFont(font)
        self.Diferencia_3.setObjectName("Diferencia_3")
        self.horizontalLayout_40.addWidget(self.Diferencia_3)
        self.Res_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_3.setFont(font)
        self.Res_3.setObjectName("Res_3")
        self.horizontalLayout_40.addWidget(self.Res_3)
        self.Lon_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_3.setFont(font)
        self.Lon_3.setObjectName("Lon_3")
        self.horizontalLayout_40.addWidget(self.Lon_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.Btn4 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn4.setFont(font)
        self.Btn4.setObjectName("Btn4")
        self.horizontalLayout_38.addWidget(self.Btn4)
        self.Diferencia_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_4.setFont(font)
        self.Diferencia_4.setObjectName("Diferencia_4")
        self.horizontalLayout_38.addWidget(self.Diferencia_4)
        self.Res_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_4.setFont(font)
        self.Res_4.setObjectName("Res_4")
        self.horizontalLayout_38.addWidget(self.Res_4)
        self.Lon_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_4.setFont(font)
        self.Lon_4.setObjectName("Lon_4")
        self.horizontalLayout_38.addWidget(self.Lon_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn5 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn5.setFont(font)
        self.Btn5.setObjectName("Btn5")
        self.horizontalLayout_2.addWidget(self.Btn5)
        self.Diferencia_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_5.setFont(font)
        self.Diferencia_5.setObjectName("Diferencia_5")
        self.horizontalLayout_2.addWidget(self.Diferencia_5)
        self.Res_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_5.setFont(font)
        self.Res_5.setObjectName("Res_5")
        self.horizontalLayout_2.addWidget(self.Res_5)
        self.Lon_5 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_5.setFont(font)
        self.Lon_5.setObjectName("Lon_5")
        self.horizontalLayout_2.addWidget(self.Lon_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Btn6 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn6.setFont(font)
        self.Btn6.setObjectName("Btn6")
        self.horizontalLayout_3.addWidget(self.Btn6)
        self.Diferencia_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_6.setFont(font)
        self.Diferencia_6.setObjectName("Diferencia_6")
        self.horizontalLayout_3.addWidget(self.Diferencia_6)
        self.Res_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_6.setFont(font)
        self.Res_6.setObjectName("Res_6")
        self.horizontalLayout_3.addWidget(self.Res_6)
        self.Lon_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_6.setFont(font)
        self.Lon_6.setObjectName("Lon_6")
        self.horizontalLayout_3.addWidget(self.Lon_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Btn7 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn7.setFont(font)
        self.Btn7.setObjectName("Btn7")
        self.horizontalLayout_4.addWidget(self.Btn7)
        self.Diferencia_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_7.setFont(font)
        self.Diferencia_7.setObjectName("Diferencia_7")
        self.horizontalLayout_4.addWidget(self.Diferencia_7)
        self.Res_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_7.setFont(font)
        self.Res_7.setObjectName("Res_7")
        self.horizontalLayout_4.addWidget(self.Res_7)
        self.Lon_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_7.setFont(font)
        self.Lon_7.setObjectName("Lon_7")
        self.horizontalLayout_4.addWidget(self.Lon_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Btn8 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn8.setFont(font)
        self.Btn8.setObjectName("Btn8")
        self.horizontalLayout_5.addWidget(self.Btn8)
        self.Diferencia_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_8.setFont(font)
        self.Diferencia_8.setObjectName("Diferencia_8")
        self.horizontalLayout_5.addWidget(self.Diferencia_8)
        self.Res_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_8.setFont(font)
        self.Res_8.setObjectName("Res_8")
        self.horizontalLayout_5.addWidget(self.Res_8)
        self.Lon_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_8.setFont(font)
        self.Lon_8.setObjectName("Lon_8")
        self.horizontalLayout_5.addWidget(self.Lon_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Btn9 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Btn9.setFont(font)
        self.Btn9.setObjectName("Btn9")
        self.horizontalLayout_6.addWidget(self.Btn9)
        self.Diferencia_9 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_9.setFont(font)
        self.Diferencia_9.setObjectName("Diferencia_9")
        self.horizontalLayout_6.addWidget(self.Diferencia_9)
        self.Res_9 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_9.setFont(font)
        self.Res_9.setObjectName("Res_9")
        self.horizontalLayout_6.addWidget(self.Res_9)
        self.Lon_9 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_9.setFont(font)
        self.Lon_9.setObjectName("Lon_9")
        self.horizontalLayout_6.addWidget(self.Lon_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.BtnPW = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BtnPW.setFont(font)
        self.BtnPW.setObjectName("BtnPW")
        self.horizontalLayout_7.addWidget(self.BtnPW)
        self.Diferencia_PW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_PW.setFont(font)
        self.Diferencia_PW.setObjectName("Diferencia_PW")
        self.horizontalLayout_7.addWidget(self.Diferencia_PW)
        self.Res_PW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_PW.setFont(font)
        self.Res_PW.setObjectName("Res_PW")
        self.horizontalLayout_7.addWidget(self.Res_PW)
        self.Lon_PW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_PW.setFont(font)
        self.Lon_PW.setObjectName("Lon_PW")
        self.horizontalLayout_7.addWidget(self.Lon_PW)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.BtnAw = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BtnAw.setFont(font)
        self.BtnAw.setObjectName("BtnAw")
        self.horizontalLayout_8.addWidget(self.BtnAw)
        self.Diferencia_AW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_AW.setFont(font)
        self.Diferencia_AW.setObjectName("Diferencia_AW")
        self.horizontalLayout_8.addWidget(self.Diferencia_AW)
        self.Res_AW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_AW.setFont(font)
        self.Res_AW.setObjectName("Res_AW")
        self.horizontalLayout_8.addWidget(self.Res_AW)
        self.Lon_AW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_AW.setFont(font)
        self.Lon_AW.setObjectName("Lon_AW")
        self.horizontalLayout_8.addWidget(self.Lon_AW)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.BtnSW = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BtnSW.setFont(font)
        self.BtnSW.setObjectName("BtnSW")
        self.horizontalLayout_9.addWidget(self.BtnSW)
        self.Diferencia_SW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Diferencia_SW.setFont(font)
        self.Diferencia_SW.setObjectName("Diferencia_SW")
        self.horizontalLayout_9.addWidget(self.Diferencia_SW)
        self.Res_SW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Res_SW.setFont(font)
        self.Res_SW.setObjectName("Res_SW")
        self.horizontalLayout_9.addWidget(self.Res_SW)
        self.Lon_SW = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Lon_SW.setFont(font)
        self.Lon_SW.setObjectName("Lon_SW")
        self.horizontalLayout_9.addWidget(self.Lon_SW)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.texCali = QtWidgets.QTextEdit(Dialog)
        self.texCali.setGeometry(QtCore.QRect(410, 580, 981, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.texCali.setFont(font)
        self.texCali.setMouseTracking(False)
        self.texCali.setAcceptDrops(False)
        self.texCali.setTabChangesFocus(False)
        self.texCali.setLineWrapColumnOrWidth(0)
        self.texCali.setObjectName("texCali")
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 580, 381, 71))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BtnLimpiar = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BtnLimpiar.setFont(font)
        self.BtnLimpiar.setObjectName("BtnLimpiar")
        self.verticalLayout_3.addWidget(self.BtnLimpiar)
        self.BtnCalibrar = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCalibrar.setFont(font)
        self.BtnCalibrar.setObjectName("BtnCalibrar")
        self.verticalLayout_3.addWidget(self.BtnCalibrar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.texCali, self.Tex5)
        Dialog.setTabOrder(self.Tex5, self.Tex6)
        Dialog.setTabOrder(self.Tex6, self.Tex7)
        Dialog.setTabOrder(self.Tex7, self.Tex8)
        Dialog.setTabOrder(self.Tex8, self.Tex9)
        Dialog.setTabOrder(self.Tex9, self.TexPW)
        Dialog.setTabOrder(self.TexPW, self.TexAW)
        Dialog.setTabOrder(self.TexAW, self.TexSW)
        Dialog.setTabOrder(self.TexSW, self.BtnCalibrar)
        Dialog.setTabOrder(self.BtnCalibrar, self.Btn5)
        Dialog.setTabOrder(self.Btn5, self.Btn6)
        Dialog.setTabOrder(self.Btn6, self.Btn7)
        Dialog.setTabOrder(self.Btn7, self.Btn8)
        Dialog.setTabOrder(self.Btn8, self.Btn9)
        Dialog.setTabOrder(self.Btn9, self.BtnPW)
        Dialog.setTabOrder(self.BtnPW, self.BtnSW)
        Dialog.setTabOrder(self.BtnSW, self.BtnAw)
        Dialog.setTabOrder(self.BtnAw, self.BtnLimpiar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Titulo4.setText(_translate("Dialog", "Longitud"))
        self.BtnEmpezar.setText(_translate("Dialog", "Empezar a Medir"))
        self.Titulo1.setText(_translate("Dialog", "Diferencia"))
        self.Titulo2.setText(_translate("Dialog", "Corto/Correcto/Largo  "))
        self.Titulo3.setText(_translate("Dialog", "Longitud"))
        self.Labt4.setText(_translate("Dialog", "Palo  3"))
        self.Labt4_3.setText(_translate("Dialog", "Palo  4"))
        self.Labt5.setText(_translate("Dialog", "Palo  5"))
        self.Labt6.setText(_translate("Dialog", "Palo  6"))
        self.Labt7.setText(_translate("Dialog", "Palo  7"))
        self.Labt8.setText(_translate("Dialog", "Palo  8"))
        self.Labt9.setText(_translate("Dialog", "Palo  9"))
        self.LabtPW.setText(_translate("Dialog", "Palo  PW"))
        self.LabtAW.setText(_translate("Dialog", "Palo  AW"))
        self.LabtSW.setText(_translate("Dialog", "Palo  SW"))
        self.Btn3.setText(_translate("Dialog", "Palo  3"))
        self.Diferencia_3.setText(_translate("Dialog", "-"))
        self.Res_3.setText(_translate("Dialog", "-"))
        self.Lon_3.setText(_translate("Dialog", "-"))
        self.Btn4.setText(_translate("Dialog", "Palo  4"))
        self.Diferencia_4.setText(_translate("Dialog", "-"))
        self.Res_4.setText(_translate("Dialog", "-"))
        self.Lon_4.setText(_translate("Dialog", "-"))
        self.Btn5.setText(_translate("Dialog", "Palo  5"))
        self.Diferencia_5.setText(_translate("Dialog", "-"))
        self.Res_5.setText(_translate("Dialog", "-"))
        self.Lon_5.setText(_translate("Dialog", "-"))
        self.Btn6.setText(_translate("Dialog", "Palo  6"))
        self.Diferencia_6.setText(_translate("Dialog", "-"))
        self.Res_6.setText(_translate("Dialog", "-"))
        self.Lon_6.setText(_translate("Dialog", "-"))
        self.Btn7.setText(_translate("Dialog", "Palo  7"))
        self.Diferencia_7.setText(_translate("Dialog", "-"))
        self.Res_7.setText(_translate("Dialog", "-"))
        self.Lon_7.setText(_translate("Dialog", "-"))
        self.Btn8.setText(_translate("Dialog", "Palo  8"))
        self.Diferencia_8.setText(_translate("Dialog", "-"))
        self.Res_8.setText(_translate("Dialog", "-"))
        self.Lon_8.setText(_translate("Dialog", "-"))
        self.Btn9.setText(_translate("Dialog", "Palo  9"))
        self.Diferencia_9.setText(_translate("Dialog", "-"))
        self.Res_9.setText(_translate("Dialog", "-"))
        self.Lon_9.setText(_translate("Dialog", "-"))
        self.BtnPW.setText(_translate("Dialog", "Palo  PW"))
        self.Diferencia_PW.setText(_translate("Dialog", "-"))
        self.Res_PW.setText(_translate("Dialog", "-"))
        self.Lon_PW.setText(_translate("Dialog", "-"))
        self.BtnAw.setText(_translate("Dialog", "Palo  AW"))
        self.Diferencia_AW.setText(_translate("Dialog", "-"))
        self.Res_AW.setText(_translate("Dialog", "-"))
        self.Lon_AW.setText(_translate("Dialog", "-"))
        self.BtnSW.setText(_translate("Dialog", "Palo  SW"))
        self.Diferencia_SW.setText(_translate("Dialog", "-"))
        self.Res_SW.setText(_translate("Dialog", "-"))
        self.Lon_SW.setText(_translate("Dialog", "-"))
        self.texCali.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:400;\">50.060</span></p></body></html>"))
        self.BtnLimpiar.setText(_translate("Dialog", "Limpiar"))
        self.BtnCalibrar.setText(_translate("Dialog", "Calibrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

