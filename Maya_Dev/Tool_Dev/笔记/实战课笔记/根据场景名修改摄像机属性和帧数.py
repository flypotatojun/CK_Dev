# -*- coding: utf-8 -*-
import pymel.core as pm
# pm.sceneName()# 返回的是对象，可以用dir(pm.sceneName()) 查看
file_name = pm.sceneName().splitext()[0].basename() # 提取maya文件名
# start_time = pm.playbackOptions(q = True,min = True) # 查找时间滑块属性，词句可以不用写
start_time = pm.env.minTime # 获取时间滑块起始帧
end_time = pm.env.maxTime # 获取时间滑块结束帧
camera_name = '%s_S%03d_E%03d' % (file_name,start_time,end_time)
# camera_list = pm.listCameras(p = True) # 查所有透视图相机
camera_list = [p_camera for p_camera in pm.listCameras(p = True) if p_camera != 'persp'] #得到新建的透视图相机名


