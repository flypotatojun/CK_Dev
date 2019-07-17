# encoding:utf-8

# import maya.standalone
# maya.standalone.initialize(name = "python")
# import maya.cmds as mc

import sys
import os

# for i in sys.path: print(i)
target = sys.argv[0]
a = target.replace("\\", "/")

print(a)

# target.replace("\\", "/")
# print(target[0])


# target_dir = os.path.split(target)
# print(type(target_dir))