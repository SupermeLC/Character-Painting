from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

color = '$&odZCzx/1?<I". '

#================================================
ori_img = Image.open('pic/im.jpg').convert('L')
width , height = ori_img.size

img = np.array(ori_img.resize((int(width * 1.4),height),Image.BILINEAR))

x,y = img.shape
pic = []


im = Image.new("RGB", (x*17, int(y*3.5)), (255, 255, 255))
dr = ImageDraw.Draw(im)

font = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc",12,index = 0)#Font

for i in range(x):
    for j in range(y):
        num = int(img[i][j]*16/255)
        pic.append(color[num])
    c = ''.join(pic)
    dr.text((10, 10 * i), c, font=font, fill="#000000")
    pic = []



im.show()
im.save('results/1.jpg')

