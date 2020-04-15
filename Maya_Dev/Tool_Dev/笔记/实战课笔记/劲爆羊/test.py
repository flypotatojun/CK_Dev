# -*- coding: utf-8 -*-
# .@FileName:test
# .@Date    :2019-07-10:16:19
# .@Author  :CK

import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
print(sys.version)

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(MyWidget, self).__init__(parent)
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
