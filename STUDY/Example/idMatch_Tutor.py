# -*- coding: utf-8 -*-
# .@FileName:idMatch_Tutor
# .@Date    :2019-06-11:14:48
# .@Author  :CK

import os
os.chdir('D:\\CK_Dev')
readNum1=[]
readNum2=[]
with open('D:\\CK_Dev\\num1.txt','r') as num1:
    readNum1 = num1.readlines()
with open('D:\\CK_Dev\\num2.txt','r') as num2:
    readNum2 = num2.readlines()

for inNum1 in readNum1:
    for inNum2 in readNum2:
        if inNum1==inNum2:
            print(inNum1)
