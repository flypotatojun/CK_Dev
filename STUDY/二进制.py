with open("test.txt",mode='w',encoding = 'utf-8') as file: #作为file打开文件, 此方法不用关闭file.close()


import pickle  # 二进制
import os
data = {'zhangsan': 1434, 'lisi': 49080}
with open('text.txt', mode='wb') as f:  # wb写入二进制文件
    pickle.dump(data, f)  # 写入data数据用dump，会动创建文件

with open('text.txt', mode='rb') as f:  # rb读取二进制文件
    of = pickle.load(f)  # 打开文件
    print(of)
