#encoding:utf-8
# python中
import os, sys
def MkDir():
    path = 'C:/Users/CK/Desktop/Sc06/'
    i = 0
    for i in range(1,49):
        s = '%03d' % i
        temp_name='E11_Sc06_Cam'+str(s)
        #maya_name = temp_name+'.ma'
        file_name = (path + temp_name)
        maya_name = (file_name+'/'+temp_name+'.ma')
        os.mkdir(file_name)
        f=open(maya_name,"w")
        f.close()
        i=i+1
        # print(maya_name)
MkDir()

# Maya中
import maya.cmds as mc
import os

def MkDir():
    path = raw_input('请输入路径：\n')+'\\'
    print(path)
    numStart = input('请输入起始帧：\n')
    print numStart
    numEnd = input('请输入结束帧：\n')
    print numEnd
    i = 0
    for i in range(numStart,numEnd+1):
        s = '%03d' % i
        temp_name='E11_Sc06_Cam'+str(s)
        file_name = (path + temp_name)
        maya_name = (file_name+'/'+temp_name+'.ma')
        if not os.path.exists(maya_name):
            mc.sysFile( file_name, makeDir=True )
            mc.file( rename=maya_name )
            mc.file(save=True)
            i+=1
        else:
            print(u'文件已存在！！！')

if __name__ == '__main__':
    MkDir()