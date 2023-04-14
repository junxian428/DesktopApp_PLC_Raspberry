from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QGridLayout,QComboBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox
import serial
import time

#global str_total
#global location
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('UI/COMM.ui', self) # Load the .ui file

          self.setWindowTitle('PLC Raspberry Pi')
          #combo_box = self.findChild(QComboBox, "comboBox")
          #combo_box.currentIndexChanged.connect(self.selectionChanged)
          self.textEdit.setText("10")
          self.textEdit_2.setText("100.01")

          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
          self.button.clicked.connect(self.printValue)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
          self.button.clicked.connect(self.exit_program)
          self.textBrowser.setText("Waiting for response...")

          self.show() # Show the GUI

  
    def printValue(self):
           PLC_Type = self.comboBox.currentText()
           Address_Type = self.comboBox_2.currentText()
            #text = self.text_edit.toPlainText()
           Station = self.textEdit.toPlainText()

           Address_Value = self.textEdit_2.toPlainText()
           Baud_Rate = self.comboBox_3.currentText()
           Parity = self.comboBox_4.currentText()
           Stop_Bits = self.comboBox_5.currentText()

           print(PLC_Type)
           print(Address_Type)
           print(Address_Value)
           print(Station)
           print(Baud_Rate)
           print(Parity)
           print(Stop_Bits)

           if(PLC_Type == "Omron PLC"):
               print("OMRON PLC")  
                # configure serial communication
               ser = serial.Serial(port='/dev/ttyUSB0', baudrate=int(Baud_Rate),   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)
               # send data over serial communication
               message = b'@10RR0004000346*\r'

               ser.write(message)
               with open('sending.txt', 'w') as file:
                   file.write(message.decode())
               ser.close()
               time.sleep(1)
               with open("response.txt", "r") as file:
                    file_contents = file.read()

               print(file_contents)
               self.textBrowser.setText(file_contents)


           elif(PLC_Type == "Delta PLC"):
              print("Delta PLC")
           else:
                print("Error")



    def exit_program(self):
          exit()

      


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


