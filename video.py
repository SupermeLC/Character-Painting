import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

color = '$&odZCzx/1?<I". '

#载入视频
vc = cv2.VideoCapture('boxing.mp4')
c = 1
n = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

#视频帧计数间隔频率
timeF = 2
#videosize(5:2)
size_1 = 200
size_2 = 80



while rval:#循环读取视频帧
    rval, frame  = vc.read()
    if(c%timeF == 0):#每隔timeF帧进行存储操作
        img_or = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img_or, (size_1,size_2), interpolation = cv2.INTER_AREA)#降低图片大小

        x, y = img.shape
        pic = []
        print("==")
        im = Image.new("RGB", (int(x * 15), int(y * 4)), (255, 255, 255))
        dr = ImageDraw.Draw(im)

        font = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 12, index=0)

        for i in range(x):
            for j in range(y):
                num = int(img[i][j] * 16 / 256)
                pic.append(color[num])
            k = ''.join(pic)
            dr.text((10, 10 * i), k, font=font, fill="#000000")
            pic = []

        im = np.array(im)
        im = cv2.resize(im, (size_1*3,size_2*5), interpolation=cv2.INTER_AREA)#降低视频大小

        cv2.imwrite('images/'+ str(n)+ '.jpg',im) #存储图像路径
        n = n+1
    c = c+1
    cv2.waitKey(1)
vc.release()

img_root = 'images/'
fps = 12    #FPS movie=24 TV=25


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('saveVideo.avi',fourcc,fps,(size_1*3,size_2*5))#与图像大小一致

for i in range(168):#图片数
    frame = cv2.imread(img_root+str(i+1)+'.jpg')
    videoWriter.write(frame)
videoWriter.release()
