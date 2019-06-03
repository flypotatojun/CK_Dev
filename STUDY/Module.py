# =================================================================
# Package 包 就是文件夹,内有许多py文件,可能有子文件夹,子文件夹里也有py文件
# 包 是文件夹, 模块 是一个文件
# python语言的 模块 和 包 相当于其他语言中的 头文件(header file) 和 库(library)
# 库 和 包 常常混称
# =================================================================
# 从文件夹(包,package)导入模块
# from . import test2  # 从本级文件夹导入test2模块

# from t3 import test3  # 从本级文件夹 的子文件夹t3导入test3模块
# print(test3.div(3, 6))

# import t3.test3  # 导入t3文件夹的test3模块
# print(t3.test3.div(3, 6))  # ！注意和上面的区别！

# import t3.test3 as tt3 # 导入t3文件夹的test3模块,并起个别名
# print(tt3.div(3, 6))  # ！注意和上面的区别！

# 复杂的包层级可能更多
# import t1.t2.t3.test3  # 按文件夹层级去找

# =================================================================
# 安装其他人制作的Python包 打开cmd
# 直接 pip 会列出可执行的指令
# pip list 列出已安装的包
# pip install packagename  安装
# pip install packagename==version  安装特定版本
# pip show packagename  查看包的版本和简介
# pip uninstall packagename  卸载
# pip install requests  请安装requests模块
# help('numpy')  # 模块的帮助文档
# =================================================================
from random import choice, randint, random,seed,shuffle
# randint 随机整数
# choice 随机选择
# random 随机0-1的浮点数，不包括1
# =================================================================
import pdb  # 导入pbd模块
# PDB -> Python Debugger
# l:list 列出附近几行代码 n:next 运行下一行  p:print 打印...
# c:continue 继续往后运行所有代码，如果再次遇到断点，会停下
# a:all 所有变量的值
# pdb.set_trace() # 设置断点，rcf运行的时候可以将右下角改成plain text
# =================================================================
# 列表推导式与Generator Expression的内存占用
from sys import getsizeof  # 从sys模块导入函数
print(getsizeof(10000))  # 一个数字 所占的内存
print(getsizeof([num * 2 for num in range(10000)]))  # 一万个数字的列表,所占的内存
print(getsizeof((num * 2 for num in range(10000))))  # 生成一万个数字,生成出来但不保存,所耗费的内存

# =================================================================
from math import ceil, floor
# ceil: 向右取整
# floor: 向左取整
# =================================================================
from os import getcwd
print(getcwd()) #获取当前文件路径
# =================================================================
