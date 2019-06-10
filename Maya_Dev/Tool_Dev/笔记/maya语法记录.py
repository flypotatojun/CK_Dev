#encoding:utf-8
'''写好的py文件保存在scripts下面，新建文件夹名称为工具包名，
文件夹内建__init__.py,工具名.py,这样在maya里可以直接import调用'''
import maya.cmds as mc
import pymel.core as pymel
import os,sys


whatIs() #在mel下面运行可以查找命令说明

import maya.mel as mel #python执行mel命令
mel.eval('select - add item')

python "import maya.cmds as mc"; #mel中执行python
python "mc.select(\'item\',r=True)"; #mel中执行python



mc.objExists(target) #判断物体是否存在
mc.waring('提示语') #提示 警告

selection = mc.ls(sl=True,l=True) #列出选择的物体,l=True表示显示长名,|pCube1,不写显示短名
for idx,item in enumerate(selection):
    # ex:|group1|pCube2 -> ['group1','pCube2']
    short_name = item.split('|')[-1]
    mc.rename(item,new_name+str(idx +1).zfill(4)) #新名字添加序列从1开始，.zfill(4)4位0001


mc.rename('item_####_grp',mc.ls(ls=True),10) #''命名格式，选择的物体，起始数字（待确认）

s=['S3_E11_Sc06_Cam003_Cam_s823e851.fbx']
''.join(s) #Result: S3_E11_Sc06_Cam003_Cam_s823e851.fbx

f='S:\QSJResources\Shot\GodGunStory\S3_E11\\'
f.replace('\\', '/') #Result: S:/QSJResources/Shot/GodGunStory/S3_E11/


allCam = mc.ls(long = True,type = "camera") #列出所有摄像机
allCam.sort(key=len, reverse=True) #按名称长度排列
renderCam = allCam[0].split('|')[1] #字符串按照|拆分开，并取第二位
renderCam2=''.join(renderCam) #连接每个字符串''中指定以什么方式连接（-，：，|）等

children = mc.listRelatives(obj,children=True, fullPath=True) or [] #获得物体的shape节点

maya_renderer = "%s/bin/Render.exe" % os.getenv("MAYA_LOCATION").replace('\\', '/')
#Result: C:/Program Files/Autodesk/Maya2016/bin/Render.exe
