# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\CK_Dev\Maya_Dev\Tool_Dev\Tools\MadGoatToolkit.ui',
# licensing of 'D:\CK_Dev\Maya_Dev\Tool_Dev\Tools\MadGoatToolkit.ui' applies.
#
# Created: Thu Jul 11 18:43:07 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(394, 379)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(MainDialog)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.splitter = QtWidgets.QSplitter(MainDialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AllToolkit = AllToolkit(self.groupBox_3)
        self.AllToolkit.setObjectName("AllToolkit")
        self.verticalLayout_6.addWidget(self.AllToolkit)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.MyFavorate = ToolsBox(self.groupBox_4)
        self.MyFavorate.setObjectName("MyFavorate")
        self.verticalLayout_8.addWidget(self.MyFavorate)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtWidgets.QApplication.translate("MainDialog", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff359d;\">图片</span></p></body></html>", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainDialog", "个人收藏", None, -1))

from ToolsBox import ToolsBox
from AllToolkit import AllToolkit

