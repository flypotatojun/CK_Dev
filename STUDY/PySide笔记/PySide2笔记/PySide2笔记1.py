# -*- coding: utf-8 -*-
# .@FileName:PySide2笔记
# .@Date    :2019-06-05:16:02
# .@Author  :CK

import sys
from PySide2.QtWidgets import QApplication, QLabel
# 从PySide2.QtWidgets中导入QApplicarion和QLabel这两个类，一个是应用程序类，一个是标签类

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 生成一个应用程序对象，传入了相关参数，这个参数是自己输入的
    label = QLabel('hello world')  # 生成一个标签对象，内容是hello world
    label.show()  # 把这个标签对象显示出来
    sys.exit(app.exec_())  # 程序结束
# 关于这个app.exec_()，exec_()这个是QtCore.QCoreApplication类中的静态方法，它的功能是进入到主事件循环，
# 然后会一直等待，当你调用QCoreApplication类中的exit()方法时会返回，返回值就是exit方法返回的值。
# 在QCoreApplication类中还有一个quit方法，如果调用quit方法，那么exit方法就会返回0，相当于调用exit(0)。
#####################################################################################################
