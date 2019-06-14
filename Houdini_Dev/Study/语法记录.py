# encoding:utf-8
import os
hou.ui.displayMessage('hello world!')  # 弹出提示框
loader = hou.node('/obj').creatNode('geo', 'OBJ_Loader')  # geo类型，obj_loader节点名
loader.creatNode('file')