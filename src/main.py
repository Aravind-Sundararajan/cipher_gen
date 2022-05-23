"""
main.py
====================================
cipher gen main driver
"""

import sys, os, time, dataclasses  # noqa
from PyQt5 import QtCore, Qt, QtGui, QtWidgets, uic  # noqa
from PyQt5.QtCore import pyqtSignal, QObject, QSettings  # noqa
from PyQt5.QtGui import QPixmap, QFont  # noqa
from PyQt5.QtWidgets import (
    QSplashScreen,
    QToolButton,
    QFileDialog,
)  # noqa

from qt_material import apply_stylesheet


class CipherMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        """Constructor for mainwindow."""
        super().__init__(*args)
        fnameUI = os.path.join(os.path.dirname(__file__), "./ui/main_gui.ui")
        uic.loadUi(fnameUI, self)
        self.setWindowTitle("Dotsies Cipher Generator")

    def set_palette(self):
        if self.palette == "light_blue.xml":
            apply_stylesheet(self.app, theme="light_blue.xml")
        else:
            apply_stylesheet(self.app, theme="dark_amber.xml")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CipherMainWindow()
    window.set_palette()
    window.app = app
    app.processEvents()
    time.sleep(0.1)
    window.show()
    sys.exit(app.exec_())
