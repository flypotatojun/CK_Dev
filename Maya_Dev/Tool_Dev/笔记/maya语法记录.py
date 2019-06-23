#encoding:utf-8
'''写好的py文件保存在scripts下面，新建文件夹名称为工具包名，
文件夹内建__init__.py,工具名.py,这样在maya里可以直接import调用'''
import maya.cmds as mc
import pymel.core as pm
import os,sys


whatIs() #在mel下面运行可以查找命令说明

import maya.mel as mel #python执行mel命令
mel.eval('select - add item')

python "import maya.cmds as mc" #mel中执行python
python "mc.select(\'item\',r=True)" #mel中执行python



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

mc.internalVar(userAppDir=True)
# Result: u'C:/Users/Administrator/Documents/maya/'

pm.workspace.getcwd() #新
pm.workspace(query=1, dir=1) #老
# 获取当前文件所在目录,maya中会返回 Result: Path('D:/') ，转成str()可以去除u,Path等字符

mc.file(q=True, sn=1, shn=1) #获取当前maya的文件名
pm.sceneName() # 获取当前maya的路径


# 获取module路径
os.environ["MAYA_MODULE_PATH"]

#返回所选路劲下文件的名字
path = os.listdir(path)

mc.file( force=True, new=True ) #新建文件
mc.polySphere() #创建一个小球
mc.file( rename='child.ma' ) #重命名
mc.file( 'path',force=True, type='mayaAscii', save=True ) #保存到指定路径



# 列出指定路径下的文件夹
import os
path = r'D:\CK_Dev\CKTOOLS'
modFile = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path,f))]
print i



#########################################################################################
#查找没有返回值的命令
//例如，先找到命令在哪个节点中，有些节点在大纲中找不到，可以在知道名字的前提下在搜索里面输入 defaultRenderGlobals 
#列出所选节点下所有的命令名
ai_driver = pm.PyNode('defaultRenderGlobals')
pm.listAttr(ai_driver)



#设置渲染属性
mc.setAttr("defaultRenderGlobals.currentRenderer", "arnold", type="string")
mc.setAttr('defaultresolution.width',1280)
mc.setAttr('defaultresolution.height',720)