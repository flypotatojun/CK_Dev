#encoding:utf-8
import maya.cmds as mc
import os
f='S:\QSJResources\Shot\GodGunStory\S3_E11\\'
f2 = '\\Provide\CameraProvide\\'
camName='S3_E11_Sc06_Cam'+str(raw_input('镜头号:'))
scPath=(f+camName+f2).replace('\\', '/')
camFile=os.listdir(scPath)
camPath=scPath+''.join(camFile)
mc.file( camPath,open=True, force=True )
