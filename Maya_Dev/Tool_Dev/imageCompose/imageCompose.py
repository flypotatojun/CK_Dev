# coding:utf-8

import os
import sys
import shutil
import time

from PIL import Image, ImageDraw, ImageFont

time = time.strftime("%Y%m%d", time.localtime())

imageSizeW = 1920
imageSizeH = 1080


class CompImages(object):
    def __init__(self, imagesPath=None, outputPath=None, imageFomat=[]):
        # self.imagesPath = os.path.dirname(__file__)
        # self.outputPath = os.path.dirname(__file__)
        self.imagesPath = sys.argv[1]
        self.outputPath = sys.argv[1]
        self.imageFomat = ['.tif', '.tiff']
        self.tempPath = (self.outputPath + '/temp/')
        self.imagesName = [i for i in os.listdir(self.imagesPath) for item in self.imageFomat if
                           os.path.splitext(i)[1] == item]
        self.imagesName.sort()
        # print(self.imagesName)
        if not os.path.exists(self.tempPath):
            os.mkdir(self.tempPath)
            # print(self.tempPath)

        self.fileName = (self.imagesName[1].split('.')[0])[0:10]
        # print(self.fileName)
        print('=' * 80)
    def addFont(self):
        # 图片间隔，也就是合并成一张图后，一共有几列
        if len(self.imagesName) < 5:
            imageColumn = len(self.imagesName)
        else:
            imageColumn = 5
        # 图片间隔，也就是合并成一张图后，一共有几行，在这里行是自适应的
        imageRow = len(self.imagesName) // 5 + 1
        # 创建一个新图
        to_image = Image.new('RGB', (imageColumn * imageSizeW, imageRow * imageSizeH))

        for it in range(0, len(self.imagesName)):
            imagePath = os.path.join(self.imagesPath, self.imagesName[it])
            img = Image.open(imagePath)
            draw = ImageDraw.Draw(img)
            fontStyle = ImageFont.truetype('arialbd.ttf', 20, encoding='uft-8')
            draw.text((20, 10), self.imagesName[it], fill=(
                255, 0, 0), font=fontStyle, align='left')
            print(imagePath)
            img.save(self.tempPath + self.imagesName[it])
        # 循环遍历，把每张图片按顺序粘贴到对应位置上（除去最后一行）
        for y in range(1, imageRow):
            for x in range(1, imageColumn + 1):
                # 重塑（统一）照片的大小
                from_image = Image.open(self.tempPath + self.imagesName[imageColumn * (y - 1) + x - 1]).resize(
                    (imageSizeW, imageSizeH), Image.ANTIALIAS)
                to_image.paste(from_image, ((x - 1) * imageSizeW, (y - 1) * imageSizeH))
                # im.paste(image, position)---粘贴image到im的position（左上角）位置
        for x in range(1, len(self.imagesName) - imageColumn * (imageRow - 1) + 1):
            from_image1 = Image.open(self.tempPath + self.imagesName[imageColumn * (imageRow - 1) + x - 1]).resize(
                (imageSizeW, imageSizeH), Image.ANTIALIAS)
            to_image.paste(from_image1, ((x - 1) * imageSizeW, (imageRow - 1) * imageSizeH))
        to_image.save(self.outputPath + '/' + str(self.fileName) + '_' + time + '.tif')
        print('=' * 80)
        print("输出路径：" + self.outputPath + '/' + str(self.fileName) + '_' + time + '.tif')

        if os.path.exists(self.tempPath):
            shutil.rmtree(self.tempPath, ignore_errors=True)
            print('---tempFile File completely deleted!!!---')
        return


if __name__ == '__main__':
    run = CompImages()
    run.addFont()
