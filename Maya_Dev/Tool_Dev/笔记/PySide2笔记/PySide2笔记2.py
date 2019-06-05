# -*- coding: utf-8 -*-
# .@FileName:PySide2笔记2
# .@Date    :2019-06-05:16:09
# .@Author  :CK

import sys
from PySide2 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

quit = QtWidgets.QPushButton("Quit")
#QPushButtion是一个按钮类，这里我们产生了一个按钮的对象quit，它的功能是点击它就退出程序
quit.resize(75, 30)
#设定这个按钮的大小
quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
#设定这个字的格式，其中QFont是一个字体格式类，它传入了3个参数，
# "Times"就类似于宋体之类的选项，18就是字号大小，QtGui.QFont.Bold表示这个字加粗
QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),
                       app, QtCore.SLOT("quit()"))
#QObject类中的connect方法，用来连接对象事件的传递，上面表示quit这个对象被点击后，系统会调用app对象中的quit方法。
quit.show()
sys.exit(app.exec_())
#在应用程序中，有的控件之间需要有关联，比如我点击一下按钮，文本框里面数字就加一。
# 在微软MFC中就是通过消息循环来实现的，但是Qt里面用信号和槽的机制来实现这个，
# 当绑定了对象和对象之间的信号和槽时，当某一个对象发出一个信号，对应对象的槽就会接收这个信号，
# 从而实现控件之间的交流。
#建立信号和槽一般使用QObject类中的connect方法。这里有一个最常用的形式，如：
#connect(sender, signal, receiver, member[, type=Qt.AutoConnection])
#sender和receiver是一个QObject类或者子类，signal和member是一个字符串类，
# 通常用SIGNAL和SLOT来进行处理一下，signal表示这个sender控件的什么行为需要被发送，比如被点击，member表示receiver控件的哪个成员进行接收这个信号，就是收到这个信号后处理什么事，比如
#QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),app, QtCore.SLOT("quit()"))
#quit这个对象被点击(clicked)后，app这个对象中的quit()方法会被调用。
#信号可以由多个控件发送，然后由一个槽来进行接收，同样，多个槽也可以接收同一个信号。
