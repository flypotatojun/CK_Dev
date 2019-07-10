# encoding:utf-8
import sys
import os
import json
from PySide2 import QtWidgets, QtCore, QtGui, QtNetwork
print(sys.version)

class TestPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TestPage, self).__init__(parent)

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
        config_path = r"D:/CK_Dev/Maya_Dev/Tool_Dev/笔记/实战课笔记/劲爆羊/test_old.json"
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
            page_widget = ToolListWgt(page_name)
            self.page_stack.addWidget(page_widget)
            self.init_tool_page(page_widget, page_tool_list)

            # connect button signals so that we can change the pages
            page_button.clicked.connect(self.change_page)

    def init_tool_page(self, page_widget, page_tool_list):
        for tool_name in page_tool_list:
            tool_item = ToolItem(tool_name)
            page_widget.addItem(tool_item)


    def change_page(self):
        # change current button's object name
        current_button = self.sender()
        button_name = current_button.objectName()
        page_name = button_name.replace("_btn", "_wgt")
        # get current widget by it's name
        current_widget = self.findChild(QtWidgets.QListWidget, page_name)
        print(current_widget)
        self.page_stack.setCurrentWidget(current_widget)


class ToolListWgt(QtWidgets.QListWidget):
    def __init__(self, obj_name, parent=None):
        super(ToolListWgt, self).__init__(parent)
        self.setObjectName("%s_page_wgt" % obj_name)

        self.setViewMode(self.IconMode)
        self.setIconSize(QtCore.QSize(60,60))


class ToolItem(QtWidgets.QListWidgetItem):
    def __init__(self, tool_name, parent=None):
        super(ToolItem, self).__init__(parent)

        # set the tool name as text of this fucking item
        self.setText(tool_name)

        # find the icon image for this fucking item. by the way,and the hover icon if there is.
        main_icon_path, hover_icon_path = self.get_icon_paths(tool_name)

        # set icons
        if os.path.isfile(main_icon_path):
            icon_pixmap = QtGui.QPixmap(main_icon_path)
        # find the script for this fucking item

        # connect a signal for excuting

        # connect a signal for executing

        # find the help info

        # add a help action for this fucking menu

        #connect a signal to show this help info

    @staticmethod
    def get_icon_paths(tool_name):
        root_path = r"D:\CK_Dev\Maya_Dev\Tool_Dev\笔记\实战课笔记\劲爆羊\Tools\tool_a"
        main_icon_name = "%s_icon.png" % tool_name
        hover_icon_name = "%s_icon_hover.png" % tool_name
        main_icon_path = os.path.join(root_path, tool_name, main_icon_name)
        hover_icon_path = os.path.join(root_path, tool_name, hover_icon_name)
        return main_icon_path, hover_icon_path



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wgt = TestPage()
    wgt.show()
    app.exec_()
