# encoding:utf-8

from PySide2 import QtWidgets, QtCore, QtGui
from MadGToolButton import MadGToolButton

class ToolsBox(QtWidgets.QWidget):
    def __init__(self, obj_name="myFavorite", tool_list=[], parent=None):
        super(ToolsBox, self).__init__(parent)

        self.setObjectName("%s_page_wgt" % obj_name)
        self.__tool_list = tool_list
        self.main_layout = QtWidgets.QGridLayout(self)
        self.creat_tool_buttons()

        # style sheet
        style_sheet = """
        QPushButton{
            border:1px solid #0000ff;
            border-radius:5px;
            color: #0000ff;
            font: bold;
        }
        QPushButton:Hover{
            border: 2px solid #00ccff;
            color: #00ccff;
            font: bold italic;
        }
        """
        self.setStyleSheet(style_sheet)

    def creat_tool_buttons(self):
        x = y = 0
        for tool_name in self.__tool_list:
            tool_btn = MadGToolButton(tool_name)
            self.main_layout.addWidget(tool_btn, x, y)
            if y == 0:
                y = 1
            else:
                y = 0
                x += 1