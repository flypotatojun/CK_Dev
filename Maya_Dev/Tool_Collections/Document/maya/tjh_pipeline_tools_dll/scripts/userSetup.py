#coding: utf-8
# build the tjh_pipeline_tools menu the first time

import pymel.core as pm
import maya.mel as mel


def buildTJHPipelineToolMenu():
    try:
        mel.eval('source tjh_pipeline_tools_Main; tjh_pipeline_tools_Main; tjh_pipeline_tools;')
    except:
        pass 
pm.general.evalDeferred('buildTJHPipelineToolMenu()')





