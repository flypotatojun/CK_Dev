# -*- coding: utf-8 -*-
# .@FileName:反编译
# .@Date    :2019-08-06:15:54
# .@Author  :CK

import os
import sys
import uncompyle6


def Decompile(path):
    if os.path.exists(path):
        for parent, dirs, files in os.walk(path):
            for file in files:
                file_name, ext = os.path.splitext(file)
                if ext == ".pyc":
                    file_path = os.path.join(parent, file)
                    print
                    "[*]Decompiling:", file_path
                    cmd = "uncompyle6 " + file_path + " > " + parent + "\\" + file_name + ".py"
                    try:
                        os.system(cmd)
                        print
                        "[+]Decompile successful.\n"
                    except Exception as e:
                        print
                        e
        print
        "[*]Finished."
    else:
        print
        "[-]Wrong Directory Path."


def main():
    if len(sys.argv) != 2:
        print
        "[*]Usage: python decompile.py [Directory Path]"
    else:
        path = sys.argv[1]
        Decompile(path)


if __name__ == "__main__":
    main()


path = "D:/CK_Dev/Maya_Dev/Tool_Collections/Document/maya/2018/scripts/ABCMaterialsTool"
Decompile( path )