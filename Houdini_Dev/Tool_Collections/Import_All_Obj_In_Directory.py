import os
import hou

#弹出选择框，框名为"select Obj Directory",文件类型为houdini文件目录
obj_dir = hou.ui.selectFile(title="Select Obj Directory", file_type=hou.fileType.Directory)
#扩展显示上面路径为绝对路径
obj_dir_expanded = hou.expandString(obj_dir)
#列出指定路径下的文件名
obj_files = os.listdir(obj_dir_expanded)

file_nodes = []
#再/obj层级创建类型为geo名字为OJB_Loader的节点
loader = hou.node('/obj').createNode('geo', "OBJ_Loader")

for obj in obj_files:
    #创建file节点
    obj_file_node = loader.createNode('file', obj)
    #设置file节点的file属性
    obj_file_node.parm('file').set(obj_dir + obj)
    obj_file_node.parm('missingframe').set(1)

    file_nodes.append(obj_file_node)

merge_objs = loader.createNode('merge', 'OBJ_Merger')

for node in file_nodes:
    merge_objs.setNextInput(node)

loader.layoutChildren()

merge_objs.setDisplayFlag(True)
merge_objs.setRenderFlag(True)



