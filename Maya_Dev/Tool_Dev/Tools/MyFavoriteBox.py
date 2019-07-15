
import os
import sys
import json
from PySide2 import QtWidgets, QtCore, QtGui
from ToolsBox import ToolsBox
from MadGToolButton import MadGToolButton

class MyFavoriteBox(ToolsBox):
    def __init__(self, obj_name="myFavorite", tool_list=[], parent=None):
        super(MyFavoriteBox, self).__init__(obj_name, tool_list, parent)
        self.setAcceptDrops(True)
        self.myFavoriteJson = os.path.join(os.path.dirname(__file__), "MyFavorite.json")
        self.loadFavorites()

    def loadFavorites(self):
        # read favoritejson
        with open(self.myFavoriteJson, "r") as json_file:
            json_str = json_file.read()
            tool_list = json.loads(json_str)
        # creat button
        for tool_name in tool_list:
            self.append_button(tool_name)
    

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

    def saveFavorite(self):
        # 1.get all button in this box
        button_liset = self._tool_list
        # 2 write into json
        with open(self.myFavoriteJson, "w") as json_file:
            json_str = json.dumps(self._tool_list)
            json_file.write(json_str)




if __name__ == "__main__":
    MyFavoriteBox()