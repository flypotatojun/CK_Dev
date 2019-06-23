# -*- coding: utf-8 -*-
import pymel.core as pm
pm.headsUpDisplay( 'HUDCameraName',s=2,b=0,lfs = 'large',ba='center',bs = 'large',dw=50,pre='cameraNames')


# pm.sceneName()# 返回的是对象，可以用dir(pm.sceneName()) 查看
file_name = pm.sceneName().splitext()[0].basename() # 提取maya文件名
# start_time = pm.playbackOptions(q = True,min = True) # 查找时间滑块属性，词句可以不用写
start_time = pm.env.minTime # 获取时间滑块起始帧
end_time = pm.env.maxTime # 获取时间滑块结束帧
camera_name = '%s_S%03d_E%03d' % (file_name,start_time,end_time)
# camera_list = pm.listCameras(p = True) # 查所有透视图相机
camera_list = [p_camera for p_camera in pm.listCameras(p = True) if p_camera != 'persp'] #得到新建的透视图相机名
selection_panel = pm.getPanel(withFocus = True)

'''面板无法切换bug
selection_camera = pm.modelPanel(selection_panel,q =True,camera = True)
camera_pynode = pm.PyNode(selection_camera)
camera_pynode.rename(camera_name)
'''

render_edit_node = pm.PyNode('defaultRenderGlobals')
pm.listAttr(render_edit_node)
render_edit_node.imageFilePrefix.set('<Scene>/<RenderLayer>')
render_edit_node.animation.set(1)
render_edit_node.startFrame.set(start_time)
render_edit_node.endFrame.set(end_time)
pm.setAttr('defaultResolution.width',1280)
pm.setAttr('defaultResolution.height',720)




