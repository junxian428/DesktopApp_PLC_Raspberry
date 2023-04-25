from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
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
          uic.loadUi('UI/Landing.ui', self) # Load the .ui file

          self.setWindowTitle('PLC Raspberry Pi')
        
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
          self.button.clicked.connect(self.loadNewUI)
          #self.button = self.findChild(QtWidgets.QPushButton, 'area')
          #self.button.clicked.connect(self.CalculateArea)
          #self.button = self.findChild(QtWidgets.QPushButton, 'WriteExcel')
          #self.button.clicked.connect(self.WriteExcelFunction)
          #pushButton_3
          #self.Canvas = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          #self.Canvas.clicked.connect(self.WriteCanvas)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
          self.button.clicked.connect(self.helloWorld)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          self.button.clicked.connect(self.exit_program)
      
          self.show() # Show the GUI
    def loadNewUI(self):
          call(["python", "CommPLC.py"])



    def exit_program(self):
          exit()

      
    def helloWorld(self):
         # configure serial communication
         ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

         # send data over serial communication
         message = b'@00WR00040001000F36*\r'

         ser.write(message)
         with open('sending.txt', 'w') as file:
            file.write(message.decode())


         # read data from serial communication
         # data = ser.readline()
         # print(str(data))
         #while True:
          #    data = ser.read(1)
        #      if data:
          #         print(data)

         # close serial communication
         ser.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


