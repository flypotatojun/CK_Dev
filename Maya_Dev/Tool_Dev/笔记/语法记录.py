#encoding:utf-8
import os
import maya.cmds as cmds
path = os.listdir(path) #返回所选路劲下文件的名字

cmds.file( force=True, new=True ) #新建文件
cmds.polySphere() #创建一个小球
cmds.file( rename='child.ma' ) #重命名
cmds.file( 'path',force=True, type='mayaAscii', save=True ) #保存到指定路径


#########################################################################################
#设置渲染属性
mc.setAttr("defaultRenderGlobals.currentRenderer", "arnold", type="string")
mc.setAttr('defaultresolution.width',1280)
mc.setAttr('defaultresolution.height',720)