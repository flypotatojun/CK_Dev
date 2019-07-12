# encoding:utf-8
import os
import sys

from PySide2 import QtWidgets, QtCore, QtGui


class MadGToolButton(QtWidgets.QPushButton):
    def __init__(self, tool_name, parent=None):
        super(MadGToolButton, self).__init__(parent)

        self.tool_name = tool_name
        # set Button text
        self.setText(self.text)
        self.setMinimumHeight(20)
        # make a context menu
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.add_context_menu_actions()
        self.clicked.connect(self.execute_script)

        self.__last_clicked_pos = None

    def add_context_menu_actions(self):
        about = QtWidgets.QAction(self)
        about.setText("about")
        self.addAction(about)

    def show_about(self):
        print(self)

    @property
    def text(self):
        text = self.tool_name
        if self.tool_dir:
            help_file_path = os.path.join(self.tool_dir, "%s_help.txt" % self.tool_name)
            with open(help_file_path) as help_file:
                text = help_file.readline()
        return text



    @property
    def tool_dir(self):
        current_dir = os.path.dirname(__file__)
        tool_dir = os.path.join(current_dir, self.tool_name)
        if os.path.isdir(tool_dir):
            return os.path.abspath(tool_dir)
        return None


    @property
    def last_clicked_pos(self):
        return self.__last_clicked_pos

    def mousePressEvent(self, event):
        super(MadGToolButton, self).mousePressEvent(event)
        self.__last_clicked_pos = (event.globalPos(), QtCore.QPoint(self.pos()))

    def mouseMoveEvent(self, event):
        if self.__last_clicked_pos:
            move, begin = self.__last_clicked_pos
            self.move((event.globalPos()-move)+begin)
        else:
            super(MadGToolButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super(MadGToolButton, self).mouseReleaseEvent(event)
        self.__last_clicked_pos = None

    def execute_script(self):
        # get script file path (glob)

        # if is a mel file, source it

        #if is a py file, execfile

        print()