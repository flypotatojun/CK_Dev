# 列出指定路径下的文件夹
import os
path = r'D:\CK_Dev\CKTOOLS'
modFile = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path,f))]
print i



