import maya.cmds as mc
import maya.mel as mel
def installCAS():
    CasShelf = [cas for cas in mc.lsUI(type = 'shelfLayout') if cas.split('|')[-1] =='CAS']
    if casShelf:
        cm.deleteUI(CasShelf[-1])
    mel.eval('loadNewShelf('shelf_CAS.mel')')

def uninstallCAS():
    CasShelf = [cas for cas in mc.lsUI(type = 'shelfLayout') if cas.split('|')[-1] =='CAS']
    if CasShelf:
        mc.deleteUI(CasShelf[-1])

def initializePlugin(mobject):
    installCAS()

def uninitializePlugin(mobject):
    uninstallCAS()
