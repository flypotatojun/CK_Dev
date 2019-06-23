import hou
import os
from hutil.Qt import QtCore,QtWidgets,QtUiTools

scriptpath = os.path.dirname(__file__)

class AttribManager(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # load UI file
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(scriptpath + '/attribman.ui')
        # Layout
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.addWidget(self.ui)
        self.setLayout(mainLayout)

def show():
    dialog = AttribManager()
    dialog.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
    dialog.show()
