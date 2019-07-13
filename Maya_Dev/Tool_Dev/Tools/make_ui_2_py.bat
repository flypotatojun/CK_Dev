@echo off

cd %~dp0
pyside2-uic -o MadGoatToolkit.py MadGoatToolkit.ui
pyside2-uic -o imgs_rc.py imgs.qrc