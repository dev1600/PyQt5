import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        #self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.setWindowTitle("MY Awesome app")
        label = QLabel("This is Awesome!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a="hello", b=5):
        print(a, b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
