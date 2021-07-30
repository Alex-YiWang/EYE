import cv2
#判断窗口点击事件
clicked = False
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
#捕获序号为0的摄像头
cameroCapture = cv2.VideoCapture(0)
#创建窗口
cv2.namedWindow('window')
#cv2.setMouseCallback('window',onMouse)
#读取帧
success,frame = cameroCapture.read()
while success and cv2.waitKey(1) == -1:
    cv2.imshow('window',frame)
    success,frame = cameroCapture.read()
cv2.destroyWindow('window')
cameroCapture.release()