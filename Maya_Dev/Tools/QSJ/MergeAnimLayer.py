#encoding:utf-8
import pymel.core as pm
import maya.cmds as mc
pm.mel.eval('animLayerMerge {%s}' % ','.join(['"%s"' % i.name() for i in pm.ls(type="animLayer")]))

