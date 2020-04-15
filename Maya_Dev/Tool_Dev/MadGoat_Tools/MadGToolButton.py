# encoding:utf-8
import os
import sys

from PySide2 import QtWidgets, QtCore, QtGui


class MadGToolButton(QtWidgets.QPushButton):
    deleteSignal = QtCore.Signal(str)
    def __init__(self, tool_name, parent=None):
        super(MadGToolButton, self).__init__(parent)

        self.tool_name = tool_name
        # set Button text
        self.setText(self.text)
        self.setFixedHeight(25)
        # make a context menu
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.add_context_menu_actions()
        self.clicked.connect(self.execute_script)



    def add_context_menu_actions(self):
        # add about action
        about_action = QtWidgets.QAction(self)
        about_action.setText("about")
        about_action.triggered.connect(self.show_about)
        self.addAction(about_action)

        # add delete action
        delete_action = QtWidgets.QAction(self)
        delete_action.setText("delete")
        delete_action.triggered.connect(self.delete_button)
        self.addAction(delete_action)


    def get_about_info(self):
        if not self.tool_dir:
            return "", ""
        help_file_path = os.path.join(self.tool_dir, "%s_help.md" % self.tool_name)
        if not os.path.isfile(help_file_path):
            return "", ""
        with open(help_file_path) as help_file:
            text = help_file.readline()
            about = help_file.read()
        return text, about


    def show_about(self):
        _, about = self.get_about_info()
        if not about:
            about = ">>>暂无描述XDDD<<<"
        title = "about %s" % self.tool_name
        QtWidgets.QMessageBox.information(None, title, about, QtWidgets.QMessageBox.Ok)

    def delete_button(self):
        self.deleteLater()
        self.deleteSignal.emit(self.tool_name)


    @property
    def text(self):
        text, _ = self.get_about_info()
        text = text.strip()
        if not text:
            text = self.tool_name
        return text



    @property
    def tool_dir(self):
        current_dir = os.path.dirname(__file__)
        tool_dir = os.path.join(current_dir, self.tool_name)
        if os.path.isdir(tool_dir):
            return os.path.dirname(tool_dir)
        return None



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            mime_data = QtCore.QMimeData()
            mime_data.setText("ToolButton_%s" % self.tool_name)
            drag = QtGui.QDrag(self)
            drag.setMimeData(mime_data)
            pixmap = QtGui.QPixmap("Maya_Dev/Tool_Dev/Tools/images/BG.jpeg").scaledToHeight(50)
            drag.setPixmap(pixmap)
            drag.exec_()
            event.accept()
        else:
            event.ignore()


    def execute_script(self):
        # get script file path (glob)

        # if is a mel file, source it

        #if is a py file, execfile

        print()