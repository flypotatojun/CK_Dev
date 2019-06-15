#encoding : utf-8
import random
import os
def idGen():
    numstr13=''
    i = 0
    while i <18:
        numstr = random.randint(0,9)
        numstr13+=str(numstr)
        i+=1
    return numstr13


with open('num1.txt','w') as num1:
    i = 0
    numstr30 = ''
    while i < 30000:
        numstr30 = idGen()
        num1.write(numstr30+'\n')
        i+=1

with open('num2.txt','w') as num2:
    i = 0
    numstr30 = ''
    while i < 30000:
        numstr30 = idGen()
        num2.write(numstr30+'\n')
        i+=1