from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox
import serial


#global str_total
#global location
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('UI/Main.ui', self) # Load the .ui file

          self.setWindowTitle('PLC Raspberry Pi')
        
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
          # create a serial object with the port name and baud rate
          # open the serial port
          ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

          # write the command to the serial port
          ser.write(b'@10MS0004000346*')
          # read the response from the PLC
          response = ser.read(100)

          print(response)
    
          ser.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


