# encoding:utf-8
from PIL import Image

# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open(r'C:\Users\chenkai\Desktop\FZ.tif')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save(r'C:\Users\chenkai\Desktop\thumbnail.jpg', 'jpeg')
