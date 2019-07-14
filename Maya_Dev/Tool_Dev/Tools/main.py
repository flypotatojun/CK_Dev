import sys
# sys.path.append(r"D:\CK_Dev\Maya_Dev\Tool_Dev\module")
# from Qt import QtWidgets, QtCore, QtGui
# from Qt.QtCompat import loadUi
from PySide2 import QtWidgets, QtCore, QtGui
from MadGoatToolkit import Ui_MainDialog



class MadGoatTookkitMain(QtWidgets.QDialog, Ui_MainDialog):
    def __init__(self, parent=None):
        super(MadGoatTookkitMain, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # widget = loadUi(ui_path)
    widget = MadGoatTookkitMain()
    widget.show()
    app.exec_()



