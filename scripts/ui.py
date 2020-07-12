# import maya.cmds
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CameraStabiliserWindow(QApplication):
    def __init__(self):
        super(CameraStabiliserWindow, self).__init__([])

        self.setApplicationDisplayName('Camera Stabiliser')

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.ui = CameraStabiliserUI()
        self.main_layout.addWidget(self.ui)

        self.main_widget.show()

        self.ui.pb_solve.clicked.connect(
            self.solve_pushed)

    def solve_pushed(self):
        ii = ['2D', '3D']
        print('Solve Pushed! Index: %s  Current Mode: %s' % (
            self.ui.tab_widget.currentIndex(),
            ii[self.ui.tab_widget.currentIndex()]))


class CameraStabiliserUI(QWidget):
    def __init__(self):
        super(CameraStabiliserUI, self).__init__(parent=None)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.tab_widget = QTabWidget()

        self.twodee = TwoDeeWidget()
        self.threedee = ThreeDeeWidget()
        self.tab_widget.addTab(self.twodee, '2D')
        self.tab_widget.addTab(self.threedee, '3D')

        self.pb_solve = QPushButton('Solve')

        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.pb_solve)


class TwoDeeWidget(QWidget):
    def __init__(self, _parent=None):
        super(TwoDeeWidget, self).__init__(parent=_parent)


class ThreeDeeWidget(QWidget):
    def __init__(self, _parent=None):
        super(ThreeDeeWidget, self).__init__(parent=_parent)
