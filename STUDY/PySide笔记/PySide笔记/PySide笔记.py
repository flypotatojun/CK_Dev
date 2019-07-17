# encoding:utf-8

import maya.cmds as mc
import maya.OpenMayaUI as omui
from PySide import QtCore, QtGui
from PySide2.QtWidgets import QLabel, QListWidget, QPushButton
from shiboken import wrapInstance


def _get_maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return  wrapInstance(long(pointer), QtGui.QWidget)

class RenamingToolWin(QtGui.QDialog):
    def __init__(self):
        super(RenamingToolWin, self).__init__(
            _get_maya_main_window())
        self._initUI()

    def _initUI(self):
        pass
if 'renaming_tool_win' in globals():  # 判断是否在变量群中
    renaming_tool_win.deleteLater()  # 删除变量
    print('# window is exists,delete it')
    del renaming_tool_win # 删除这个窗口
renaming_tool_win = RenamingToolWin()
renaming_tool_win.show()
