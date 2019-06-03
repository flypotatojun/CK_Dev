import maya.cmds as mc
import os
#导入摄像机
f='S:\QSJResources\Shot\GodGunStory\S3_E11\\'
f2 = '\\Provide\CameraProvide\\'
camName='S3_E11_Sc06_Cam'+str(raw_input('镜头号:'))
folderName='E11_Sc06_Cam'+str(raw_input('镜头号:'))
scPath=(f+camName+f2).replace('\\', '/')
camFile=os.listdir(scPath)
camPath=scPath+''.join(camFile)
mc.file( camPath,open=True, force=True )

mc.namespace( add='Cam' )
#修改摄像机名
allCam = mc.ls(long = True,type = "camera")
allCam.sort(key=len, reverse=True)
renderCam = allCam[0].split('|')[1]
renderCam2=''.join(renderCam)

#添加namespace
mc.select(renderCam2,r=True)
mc.rename(renderCam2, 'Cam:'+renderCam2)

saveFile = 'S:\\QSJResources\\Shot\FINAL\\5.15\\'+folderName+'\\'+folderName+'.ma'

cmds.file( rename=saveFile )
cmds.file( force=True, type='mayaAscii', save=True )



