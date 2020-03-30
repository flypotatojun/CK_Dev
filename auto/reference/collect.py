# encoding:utf-8
import os

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList

def my_cmp(v1, v2):
    p = re.compile("(\d+)")
    d1 = [int(i) for i in p.findall(v1)][0]
    d2 = [int(i) for i in p.findall(v2)][0]
    return cmp(d1, d2)


def main():
    # parse arguments
 
    #begin to work with a serial of images in the imgDir
    imgDir = r"M:\BLK\Season_06\\Output\BLK06_EP01\\Keyframe"
    # imgs = os.listdir(imgDir)
    # imgNum = len(imgs)
    list = GetFileList(imgDir, [])
    list.sort(my_cmp)
    for e in list[1:]:
        print(e)

        frame = detector.detect_draw_on_frame(mio.import_image(filepath=e)