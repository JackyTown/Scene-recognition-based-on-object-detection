import cv2 
import numpy
import os
from video_test import scene 
command = "python video_test.py"
videoCapture = cv2.VideoCapture()
videoCapture.open('test.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
ret,frame = videoCapture.read()
size = (frame.shape[1],frame.shape[0])
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print(size)
videowriter = cv2.VideoWriter("detection.avi",cv2.VideoWriter_fourcc('M','J','P','G'),int(fps),size)
font=cv2.FONT_HERSHEY_SIMPLEX#使用默认字体
print("fps=",fps,"frames=",frames)
for i in range(int(frames)):
        ret,frame = videoCapture.read()
        cv2.imwrite("middle.jpg",frame) #截取视频流中的某一帧画面
        s = scene()
        prediction_pic = cv2.imread("predictions.jpg") #读取网络的输出图片(带有box)
        img=cv2.putText(prediction_pic,s,(0,40),font,1.2,(255,255,255),2) #将场景识别的结果(图片分类)写入图片
        videowriter.write(img) #将图片写回视频流
print("Done!")
