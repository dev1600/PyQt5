import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        label = QLabel("this is a PyQt5 window")
        label.setAlignment(Qt.AlignCenter)
        # it sets my label in centre because of setCentrewidget()
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        self.setWindowIcon(QIcon("IconsUi/bug.png"))
        # print(QFile.exists('PyQt_Actions_and_toolbars.py'))
        # it adds button on my toolbar
        button_action = QAction(QIcon("IconsUi/bug.png"), "Button", self)
        # button_action.setIcon(QIcon("bug.png"))
        # setstatusTip() gives me text i want the user to see when he/she hovers over a button
        button_action.setStatusTip("This is your button")
        # Setting for how i want my icons and button to appear
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # triggered is when i want to connect a function to button when it is clicked
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # Gives me True when I click  the button basically functions like a toggle ie on\off
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action2 = QAction(QIcon("IconsUi/android.png"), "Button2", self)
        button_action2.setStatusTip("This is your 2nd button")
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
