from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox

global str_total
global location
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('UI/Main.ui', self) # Load the .ui file
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
          self.button.clicked.connect(self.helloWorld)
          #self.button = self.findChild(QtWidgets.QPushButton, 'area')
          #self.button.clicked.connect(self.CalculateArea)
          #self.button = self.findChild(QtWidgets.QPushButton, 'WriteExcel')
          #self.button.clicked.connect(self.WriteExcelFunction)
          #pushButton_3
          #self.Canvas = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          #self.Canvas.clicked.connect(self.WriteCanvas)
          self.show() # Show the GUI


    def helloWorld(self):
          print("Hello World")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


