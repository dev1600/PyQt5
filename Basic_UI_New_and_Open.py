# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Basic_UI_New_and_Open.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 701, 281))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_file = QtWidgets.QAction(MainWindow)
        self.new_file.setObjectName("new_file")
        self.open_file = QtWidgets.QAction(MainWindow)
        self.open_file.setObjectName("open_file")
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.menuFile.addAction(self.new_file)
        self.menuFile.addAction(self.open_file)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.new_file.triggered.connect(
            lambda: self.clicked("You Clicked New File"))
        self.open_file.triggered.connect(
            lambda: self.clicked("You Clicked Open File"))
        self.save.triggered.connect(
            lambda: self.clicked("You Clicked Save File"))
        self.save_as.triggered.connect(
            lambda: self.clicked("You Clicked Save As File"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI"))
        self.label.setText(_translate(
            "MainWindow", "I\'ll tell you  about your current action"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.new_file.setText(_translate("MainWindow", "New File"))
        self.new_file.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_file.setText(_translate("MainWindow", "Open File"))
        self.open_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.save_as.setText(_translate("MainWindow",  "Save as"))
        self.save_as.setShortcut(_translate("MainWindow", "Ctrl+T"))

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
