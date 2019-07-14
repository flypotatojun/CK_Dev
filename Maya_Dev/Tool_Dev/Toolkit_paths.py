
import os
import sys



class Tool_paths():
    def __init__(self):
        pass
    def module_path(self):
        self.module_path = os.getcwd()
        return self.module_path

a = Tool_paths()
print(a.module_path())


self.module_path()