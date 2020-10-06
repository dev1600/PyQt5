# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layout_Prototype.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
import cv2
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
import CameraFullScreenProtoype


class CameraThread(QThread):
    changePixmap = pyqtSignal(QImage)

    def TakeScreenshot(self):
        Ui_MainWindow.logic = 1

    def setFullScreen(self):
        if Ui_MainWindow.full_screen == 1:
            Ui_MainWindow.full_screen = 0
        else:
            Ui_MainWindow.full_screen = 1

    def run(self):
        cap = cv2.VideoCapture(0)
        value = 0
        while True:
            ret, frame = cap.read()
            if ret:

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(
                    rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                # print(Ui_MainWindow.full_screen)
                if Ui_MainWindow.full_screen == 0:
                    p = convertToQtFormat.scaled(480, 480, Qt.KeepAspectRatio)
                else:
                    p = convertToQtFormat.scaled(620, 480, Qt.KeepAspectRatio)

                self.changePixmap.emit(p)
                if Ui_MainWindow.logic == 1:
                    value += 1
                    cv2.imwrite(
                        'C:/Users/Devansh/Python/PyQt5 Codes/PyQt5 Designer/Screenshot/CamPhotoNo.%s.png' % (value), frame)
                    Ui_MainWindow.logic = 0
                    print("SS taken")


class Ui_MainWindow(QWidget):
    logic = 0
    full_screen = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.CameraWindow = QtWidgets.QLabel(self.centralwidget)
        #self.CameraWindow = QLabelClickable(self)
        self.CameraWindow.setGeometry(QtCore.QRect(250, 40, 271, 311))
        self.CameraWindow.setFrameShape(QtWidgets.QFrame.WinPanel)
        # self.CameraWindow.resize(480, 480)
        self.CameraWindow.setObjectName("CameraWindow")
        # self.CameraWindow.clicked.connect(self.setImage)

        self.Screenshot = QtWidgets.QPushButton(self.centralwidget)
        self.Screenshot.setGeometry(QtCore.QRect(200, 390, 141, 41))
        self.Screenshot.setObjectName("Screenshot")
        self.Screenshot.clicked.connect(CameraThread.TakeScreenshot)

        self.FullScreen = QtWidgets.QPushButton(self.centralwidget)
        self.FullScreen.setGeometry(QtCore.QRect(370, 390, 151, 41))
        self.FullScreen.setObjectName("FullScreen")
        self.FullScreen.clicked.connect(CameraThread.setFullScreen)
        self.FullScreen.setText("Toggle")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.initUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @pyqtSlot(QImage)
    def setImage(self, image):
        # while self.full_screen == 1:
        # self.full_screen = 0
        # print(self.full_screen)
        if(self.full_screen == 1):
            self.CameraWindow.setGeometry(QtCore.QRect(0, -10, 611, 491))
            self.FullScreen.setGeometry(QtCore.QRect(694, 522, 81, 31))
            self.Screenshot.setGeometry(QtCore.QRect(690, 482, 91, 31))

        else:
            self.CameraWindow.setGeometry(QtCore.QRect(250, 40, 271, 311))
            self.FullScreen.setGeometry(QtCore.QRect(370, 390, 151, 41))
            self.Screenshot.setGeometry(QtCore.QRect(200, 390, 141, 41))

        # th2 = Full(self, window)
        # th2.start()
        # new_window.CameraLabel.setPixmap(QPixmap.fromImage(image))
        # window.show()
        # th2 = Full(self)
        # th2.start()

        self.CameraWindow.setPixmap(QPixmap.fromImage(image))

    def initUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CameraWindow.setText(_translate("MainWindow", "TextLabel"))
        self.Screenshot.setText(_translate("MainWindow", "Screenshot"))
        self.FullScreen.setText(_translate("MainWindow", "Toggle"))
        th = CameraThread(self)
        th.changePixmap.connect(self.setImage)
        th.start()


# if __name__ == "__main__":
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()

window = QtWidgets.QMainWindow()
new_window = CameraFullScreenProtoype.Ui_MainWindow()
new_window.setupUi(window)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
