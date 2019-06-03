#encoding:utf-8
import maya.cmds as cmds
render_glob = "defaultRenderGlobals"
list_Attr = cmds.listAttr(render_glob, r=True, s=True)
for attr in list_Attr:
    get_attr_name = "%s.%s"%(render_glob, attr)
    print "setAttr %s %s"%(get_attr_name, cmds.getAttr(get_attr_name))