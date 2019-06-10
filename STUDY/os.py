#encoding:utf-8
shutil模块提供了copyfile()的函数
import shutil
import os
help(os.putenv)  # ->获取帮助
os.sep  # ->'\\'路径分割
os.name  # ->'nt'返回系统类型
os.getcwd()  # ->'显示当前路径'
os.chdir('路径')  # ->更改当前显示的路径
os.getenv('path')  # ->获取系统变量路径，path为系统变量默认名
os.getenv('os')  # ->获取系统名
os.putenv('name', 'path')  # ->添加环境变量name变量名，path变量路径
os.listdir(.)  # ->.表示当前目录，也可填入路径
file.close()  # 关闭文件
file.closed  # True 判断是否关闭了文件
os.remove('text.txt')  # 删除文件
os.system('notepad')  # 系统直接调用CMD打开文本编辑器，返回值0表示正常
os.startfile('路径')  # 打开文件
os.path.isdir('dir')  # 判断dir是不是路径
'''
列出当前目录下所有目录：
[x for x in os.listdir('.') if os.path.isdir(x)]
列出当前目录下所有.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
'''
os.walk('.') #方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情
'''
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
'''
os.path.isfile('dir')  # 判断dir是不是文件
os.path.abspath('.')  # 获取当前目录的绝对路径
os.path.splitext('/path/to/file.txt')  # ->获取扩展名
os.path.splitdrive('/path/to/file.txt') #分割盘符和路径
os.path.split('/Users/michael/testdir/file.txt') #分割最后一个目录或文件
os.path.join('/Users/michael', 'testdir') #拼接目录
os.mkdir('/Users/michael/testdir')  # 创建目录
os.rmdir('/Users/michael/testdir')  # 删除指定目录，该目录下不能有东西，否则报错OSError
os.removedirs('路径')  # 递归移除目录
os.chmod('路径',mode)  # 改变目录权限
os.makedirs('dir\\test\\testdir', exist_ok=False)  # 一次性创建多个文件夹,如果目录不存在
os.removedirs('dir\\test\\testdir') #删除该目录下所有目录，目录必须为空
os.path.exists('') #判断文件是否存在
os.path.basename('/Users/michael/testdir/file.txt') #返回文件名和后缀
os.path.dirname('/Users/michael/testdir/file.txt') #返回目录部分
