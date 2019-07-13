# coding:utf-8
import sys
import os
import json
from PySide2 import QtWidgets, QtCore, QtGui


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
        config_path = r"D:/CK_Dev/Maya_Dev/Tool_Dev/笔记/实战课笔记/劲爆羊/test.json"
        if not os.path.isfile(config_path):
            raise Exception('config is not found.....')
        with open(config_path, "r") as json_file:
            json_str = json_file.read()
            page_info_dict = json.loads(json_str)


        # creat page buttons
        for page_name in page_info_dict:
            # create the button
            page_button = QtWidgets.QPushButton(page_name)
            page_button.setObjectName("%s_page_btn" % page_name)
            self.button_layout.addWidget(page_button)
            # create the widget
            page_widget = QtWidgets.QListWidget()
            page_widget.setObjectName("%s_page_wgt" % page_name)
            self.page_stack.addWidget(page_widget)
            for tool in page_info_dict[page_name]:
                page_widget.addItem(QtWidgets.QListWidgetItem(tool))
            page_button.clicked.connect(self.change_page)

    def change_page(self):
        # change current button's object name
        current_button = self.sender()
        button_name = current_button.objectName()
        print(button_name)
        page_name = button_name.replace("_btn", "_wgt")
        # get current widget by it's name
        current_widget = self.findChild(QtWidgets.QWidget, page_name)
        print(current_widget)
        self.page_stack.setCurrentWidget(current_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wgt = TestPage()
    wgt.show()
    app.exec_()
