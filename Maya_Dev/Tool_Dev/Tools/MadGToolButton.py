# encoding:utf-8

from PySide2 import QtWidgets, QtCore, QtGui


class MadGToolButton(QtWidgets.QPushButton):
    def __init__(self, tool_name, parent=None):
        super(MadGToolButton, self).__init__(parent)

        self.setText(tool_name)
        self.setMinimumHeight(20)

        # make a context menu
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.add_context_menu_actions()
        # self.menu = QtWidgets.QMenu(self)
        # about = QtWidgets.QAction(self)
        # about.setText("About")
        # self.menu.addAction(about)
        # about.triggered.connect(self.show_about)

        self.__last_clicked_pos = None

    def add_context_menu_actions(self):
        about = QtWidgets.QAction(self)
        about.setText("about")
        self.addAction(about)

    def show_about(self):
        print(self)


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


    # def contextMenuEvent(self, event):
    #     self.menu.exec_(QtGui.QCursor.pos())

