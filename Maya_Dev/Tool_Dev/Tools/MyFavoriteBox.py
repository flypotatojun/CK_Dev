from PySide2 import QtWidgets, QtCore, QtGui
from ToolsBox import ToolsBox
from MadGToolButton import MadGToolButton

class MyFavoriteBox(ToolsBox):
    def __init__(self, obj_name="myFavorite", tool_list=[], parent=None):
        super(MyFavoriteBox, self).__init__(obj_name, tool_list, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().text().startswith("ToolButton"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        tool_name = event.mimeData().text()
        tool_name = tool_name.split("ToolButton_")[-1]
        if tool_name not in self._tool_list:
            # creat a tool button in this box
            self.append_button(tool_name)





if __name__ == "__main__":
    MyFavoriteBox()