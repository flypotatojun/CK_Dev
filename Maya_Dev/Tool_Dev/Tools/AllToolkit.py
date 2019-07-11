# encoding:utf-8
import sys
import os
import glob
import json
from PySide2 import QtWidgets, QtCore, QtGui
from ToolsBox import ToolsBox

class AllToolkit(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AllToolkit, self).__init__(parent)

        main_layout = QtWidgets.QVBoxLayout(self)
        self.button_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(self.button_layout)

        # creat a stracked widget and add in main layout
        self.page_stack = QtWidgets.QStackedWidget()
        main_layout.addWidget(self.page_stack)

        # creat buttons and pages then put them in button layout
        self.init_pages()

    def init_pages(self):
        # get pages info from config file
        config_path = r"D:/CK_Dev/Maya_Dev/Tool_Dev/Tools/ToolList.json"
        if not os.path.isfile(config_path):
            raise Exception('config is not found.....')
        with open(config_path, "r") as json_file:
            json_str = json_file.read()
            tool_info_list = json.loads(json_str)



        # creat page buttons
        for tool_info_dict in tool_info_list:
            page_name = tool_info_dict.get("name")
            page_tool_list = tool_info_dict.get("tool_list")

            # create the button
            page_button = QtWidgets.QPushButton(page_name)
            page_button.setObjectName("%s_page_btn" % page_name)
            self.button_layout.addWidget(page_button)

            # create the widget
            page_widget = ToolsBox(page_name, page_tool_list)
            self.page_stack.addWidget(page_widget)


            # connect button signals so that we can change the pages
            page_button.clicked.connect(self.change_page)



    def change_page(self):
        # change current button's object name
        current_button = self.sender()
        button_name = current_button.objectName()
        page_name = button_name.replace("_btn", "_wgt")
        # get current widget by it's name
        current_widget = self.findChild(ToolsBox, page_name)
        self.page_stack.setCurrentWidget(current_widget)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wgt = AllToolkit()
    wgt.show()
    app.exec_()
