# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MadGoatToolkit.ui',
# licensing of 'MadGoatToolkit.ui' applies.
#
# Created: Fri Jul 12 20:09:25 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(587, 672)
        MainDialog.setStyleSheet("QDialog{\n"
"    background-color: #00263e;\n"
"    \n"
"}\n"
"\n"
"QGroupBox{\n"
"color: rgb(170, 255, 255);\n"
"border:2px solid gray;\n"
"border-radius:5px;\n"
"margin-top:1ex;\n"
"subcontrol-origin: margin;\n"
"subcontrol-position: top center;\n"
"padding: 0 3px;\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(MainDialog)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.splitter = QtWidgets.QSplitter(MainDialog)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"\n"
"    color: rgb(241, 194, 83);\n"
"}\n"
"\n"
"QPushButton{\n"
"            border-radius:5px;\n"
"            background-color: #004877;\n"
"            color: #CFD8DC;\n"
"            font: bold;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"            border-radius:5px;\n"
"            background-color: #0081bc;\n"
"            color: #ECEFF1;\n"
"            font: bold;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AllToolkit = AllToolkit(self.groupBox_3)
        self.AllToolkit.setStyleSheet("")
        self.AllToolkit.setObjectName("AllToolkit")
        self.verticalLayout_6.addWidget(self.AllToolkit)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.MyFavorate = MyFavoriteBox(self.groupBox_4)
        self.MyFavorate.setObjectName("MyFavorate")
        self.verticalLayout_8.addWidget(self.MyFavorate)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtWidgets.QApplication.translate("MainDialog", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff359d;\">图片</span></p></body></html>", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainDialog", "个人收藏", None, -1))

from MyFavoriteBox import MyFavoriteBox
from AllToolkit import AllToolkit
import imgs_rc
