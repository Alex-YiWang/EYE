# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:24:22 2021

@author: Kirito
"""

# 导入库
import cv2
# 加载人脸识别模型
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 打开摄像头
capture = cv2.VideoCapture(0)
# 人脸检测
while True:
    # 获取摄像头捕捉的画面（帧）
    ret, frame = capture.read()
    # 将获取的画面灰度处理
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 检测人脸获取人脸区域
    faces = face_engine.detectMultiScale(gray)
    # 标记人脸区域
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 显示画面
    cv2.imshow('press q to quit', frame)
    # 按‘q’退出程序
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 释放资源
capture.release()
# 关闭窗口
cv2.destroyAllWindows()