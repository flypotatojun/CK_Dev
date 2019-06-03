import maya.cmds as cmds
import maya.mel as mel

render_cam = 'persp'
def change_render_cam(render_cam):
    render_cam_shape = cmds.listRelatives(render_cam, shapes=1)[0]
    cam_list = cmds.ls(type='camera')
    for cam_shap in cam_list:
        if cam_shap != render_cam_shape:
            cmds.setAttr("%s.renderable"%cam_shap, 0)
        else:
            cmds.setAttr("%s.renderable"%cam_shap, 1)
    # mel.eval('unifiedRenderGlobalsWindow;') #注销这一行不弹渲染窗口，对功能无影响

change_render_cam(render_cam)