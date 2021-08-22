# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:24:22 2021

@author: Kirito
"""

# 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 打开摄像头
camera = cv2.VideoCapture(0)

# 获取摄像头数据
def Get_Img(camera):
    
    # 获取摄像头捕捉的画面（帧）
    ret, RGB_Img = camera.read()
    
    return ret, RGB_Img

# 功能0 图像展示
def Img_Show():
    while True:
        ret, RGB_Img = Get_Img(camera)
        cv2.imshow('press q to quit', RGB_Img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break    

# 功能0-1 plt图像展示,会出现帧数问题
def Img_Show_1():
    #plt.ion()
    while True:
        ret, RGB_Img = Get_Img(camera)
        plt.imshow(RGB_Img)
        plt.pause(0.2)
        plt.close()

# 功能0-2 图像二值化
def custom_threshold():
    while True:
        ret, RGB_Img = Get_Img(camera)
        gray = cv2.cvtColor(RGB_Img,cv2.COLOR_RGB2GRAY)#要二值化图像，要先进行灰度化处理
        h,w=gray.shape[:2]
        m = np.reshape(gray,[1,w*h])#将图像转一维数组，一行，w*h列，转换维度要保证其size不变
        mean = m.sum() / (w*h)#求平均值来当做阈值，来分割图像
        print("mean :",mean)
        ret,binary = cv2.threshold(gray,mean,255,cv2.THRESH_BINARY)
        cv2.imshow('press q to quit', binary)
        # 按‘q’退出程序
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break      
    
# 功能1 人脸检测
def Face_detect():
    # 加载人脸识别模型
    face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    # 人脸检测
    while True:
        ret, RGB_Img = Get_Img(camera)
                
        # 将获取的画面灰度处理
        gray = cv2.cvtColor(RGB_Img, cv2.COLOR_RGB2GRAY)
        # 检测人脸获取人脸区域
        faces = face_engine.detectMultiScale(gray)
        # 标记人脸区域
        for(x, y, w, h) in faces:
            cv2.rectangle(RGB_Img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 显示画面
        
        cv2.imshow('press q to quit', RGB_Img)
        # 按‘q’退出程序
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break




def main():
    custom_threshold()
    # 释放资源
    camera.release()
    # 关闭窗口
    cv2.destroyAllWindows()

    
main()
