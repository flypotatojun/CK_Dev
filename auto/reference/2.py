# encoding:utf-8
import os

dataPath = r'M:\BLK\Season_06\Output\BLK06_EP01\Keyframe'
print(dataPath)
allName = os.listdir(dataPath)
 
allTestDataName = []
for filename in os.listdir(dataPath):
    if filename.endswith('.tiff') and not('PRE' in filename):#文件名中不包含'pre'字符串
        #print(filename)
        allTestDataName.append(filename)
 
 
allTestDataName.sort(key= lambda x:int(x[:-4]))
print(allTestDataName)
