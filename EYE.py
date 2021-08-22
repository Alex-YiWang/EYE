# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:51:57 2021

Project EYE 

@author: Kirito
"""

import sys
import cv2
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow


class EYE(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EYE, self).__init__(parent)
        self.Set_UI()


    #图形用户界面的设置
    def Set_UI(self):
        
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	btnDemo = EYE()
	btnDemo.show()
	sys.exit(app.exec_())