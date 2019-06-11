#encoding:utf-8
'''
变量命名规范：
可用数字 字母 下划线组合
不能以数字开头 如 10apple 语法错误
普通变量推荐格式:
字母开头;下划线隔开单词;全小写; 如: female_cat
常量: 全大写;下划线隔开单词 如: FEMALE_CAT
类：单词首字母大写;无下划线 如: FemaleCat
# ===============================================================
Sublime Text Tips
1.安装 Python 3 [记得勾上add path]
2.安装和配置 Sublime Text 3
	1)安装 Package Control
	2)安装 SideBarEnhancements
	3)安装 A File Icon
	4)安装 Anaconda  [http://damnwidget.github.io/anaconda/IDE/]
	5)运行 0_Hello_World.py
	6)改变 Theme[可选]
	7)安装 BufferScroll (在网盘) [https://github.com/titoBouzout/BufferScroll]
    8)安装 SublimeREPL [https://github.com/wuub/SublimeREPL]



Ctrl + 鼠标点击可以出现多个光标，同时编辑，Alt + 中键去掉某个光标;不按Ctrl单击鼠标可以退出
选中一段字符，按引号键可将其引起来

将tab缩进设为四个空格：
    命令面板 indentation: Convert to Spaces
运算符优先级 http: // www.runoob.com / python / python - operators.html  # ysf8

Preferences => Settings-Syntax Specific 在右边的Python Settings
写入 "translate_tabs_to_spaces": true
这样新建的py文件默认就是tab转成空格

CTRL + SHIFT +B 选择解释器

Shift + 鼠标右键滑动 可实现竖向多光标
# ==========================================================
 Anaconda->Settings-User 忽略某些PEP8规范
"pep8_ignore":
    [
        "E309",
        "E201",
        "E202",
        "E231",
        "E225",
    ],



# ===============================================================
# 格式转换
# 使用:.0f控制小数位
money = 20000
robbers = 5
print(f'{robbers}劫匪没人分到了{(money/robbers):.0f}元')
print('请输入')
CNY = input()
print(CNY)
# ===============================================================


# ===============================================================
print('=' * 30)  # 打印30个等号
# ===============================================================
# range()生成一个可迭代的对象，通过list()可将其转成列表
# range(start, stop=None, step=1)
# range(2)生成0和1，不包括2
# range(1, 3)生成1和2，不包括3
# range(1, 7, 2)生成1 3 5 不包括7
# range(7, 1, -1)生成7 6 5 4 3 2 不包括1
x = range(2)
print(type(x))
print(list(x))
# ===============================================================
 
转义字符
\   在行尾时 续行符
\\  反斜杠符号
\'  单引号
\"  双引号
\a  响铃
\b  退格(Backspace)
\e  转义
\000    空
\n  换行
\v  纵向制表符
\t  横向制表符
\r  回车
\f  换页
\oyy    八进制数，yy代表的字符，例如：\o12代表换行
\other  其它的字符以普通格式输出

# ===============================================================

'\U0001f62d'  # 哭脸
'\U0001f600'  # 笑脸
# ===============================================================

# 大写字母变成小写字母 lower()
# input().lower()
# ===============================================================

# print(a.pop(3))  # 移除指定序号的元素
# a.remove('0')  # 移除列表中首个值为'0'的元素
# ===============================================================

import requests as rq
r = rq.get('https://www.baidu.com/')  # 获取(GET)百度的响应(Response)
r = rq.get('http://www.sina.com.cn/sadas')  # 获取新浪的响应
print(r.url)  # 网址
r.encoding = 'utf-8'  # 改变网页编码
print(r.text)  # 网页正文代码
print(r.encoding)
print(r.headers)  # Http标头
print(r.status_code)  # Http状态码
# ===============================================================

'''
#maya中运行sublimeText

# if it was already open under another configuration
cmds.commandPort(name=":7002", close=True)

# now open a new port
cmds.commandPort(name=":7002", sourceType="python")

# or open some random MEL port (make sure you change it to this port in your config file)
cmds.commandPort(name=":10000", sourceType="mel")













'''