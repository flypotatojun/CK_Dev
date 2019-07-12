# encoding:utf-8

from PySide2 import QtWidgets, QtCore, QtGui
from MadGToolButton import MadGToolButton

class ToolsBox(QtWidgets.QWidget):
    def __init__(self, obj_name, tool_list, parent=None):
        super(ToolsBox, self).__init__(parent)


        self.setObjectName("%s_page_wgt" % obj_name)
        self._tool_list = []


        self.main_layout = QtWidgets.QGridLayout(self)


                # init tool buttons
        for tool_name in tool_list:
            self.append_button(tool_name)


        # style sheet
        style_sheet = """
        QPushButton{
            border:1px solid #0000ff;
            border-radius:5px;
            color: #0000ff;
            font: bold;
            vertical-align: middle
        }
        QPushButton:Hover{
            border: 2px solid #00ccff;
            color: #00ccff;
            font: bold italic;
        }
        """
        self.setStyleSheet(style_sheet)

    def append_button(self, button_name):
        count = len(self._tool_list)
        row = count / 2
        col = count % 2
        button = MadGToolButton(button_name)
        self.main_layout.addWidget(button, row, col)
        self._tool_list.append(button_name)


