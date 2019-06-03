'''先运行此脚本再导入角色动画'''
import maya.cmds as mc
import os
#导入摄像机
f='S:\QSJResources\Shot\GodGunStory\S3_E11\\'
f2 = '\\Provide\CameraProvide\\'
userInput=raw_input('镜头号:')
camName='S3_E11_Sc06_Cam'+str(userInput)
folderName='E11_Sc06_Cam'+str(userInput)
scPath=(f+camName+f2).replace('\\', '/')
camFile=os.listdir(scPath)
camPath=scPath+''.join(camFile)
mc.file( camPath,i=True, force=True )

#设置渲染器和帧率
#mc.setAttr("defaultRenderGlobals.currentRenderer", "arnold", type="string")
mc.currentUnit(t='pal');

mc.namespace( add='Cam' )
#修改摄像机名
allCam = mc.ls(long = True,type = "camera")
allCam.sort(key=len, reverse=True)
renderCam = allCam[0].split('|')[1]
renderCam2=''.join(renderCam)

#摄像机添加namespace
mc.select(renderCam2,r=True)
mc.rename(renderCam2, 'Cam:'+renderCam2)

#修改摄像机属性
camNewName= 'Cam:'+allCam[0].split('|')[2]
mc.setAttr (camNewName+".displayResolution",1)
mc.setAttr (camNewName+".displayGateMaskOpacity",1)
mc.setAttr (camNewName+".displaySafeAction",1)
mc.setAttr (camNewName+".filmFit",3)
mc.setAttr ('Cam:'+renderCam+".tx",lock=True)
mc.setAttr ('Cam:'+renderCam+".ty",lock=True)
mc.setAttr ('Cam:'+renderCam+".tz",lock=True)
mc.setAttr ('Cam:'+renderCam+".rx",lock=True)
mc.setAttr ('Cam:'+renderCam+".ry",lock=True)
mc.setAttr ('Cam:'+renderCam+".rz",lock=True)
mc.setAttr ('Cam:'+renderCam+".sx",lock=True)
mc.setAttr ('Cam:'+renderCam+".sy",lock=True)
mc.setAttr ('Cam:'+renderCam+".sz",lock=True)
mc.setAttr ('Cam:'+renderCam+".v",lock=True)
mc.setAttr ('Cam:'+renderCam+".fl",lock=True)



#保存文件到指定路径
mc.sysFile( 'S:\\QSJResources\\Shot\FINAL\\5.15\\'+folderName+'\\', makeDir=True )

saveFile = 'S:\\QSJResources\\Shot\FINAL\\5.15\\'+folderName+'\\'+folderName+'.ma'
mc.file( rename=saveFile )
mc.file( force=True, type='mayaAscii', save=True )





