from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QGridLayout,QComboBox, QMessageBox
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
import tkinter as tk

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
          self.textEdit_2.setText("4.01")

          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
          self.button.clicked.connect(self.printValue)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
          self.button.clicked.connect(self.exit_program)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          self.button.clicked.connect(self.generate_checksum_query)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
          self.button.clicked.connect(self.refresh)
          self.textBrowser.setText("Waiting for response...")

          self.show() # Show the GUI

   

        ###################################

    def generate_checksum_query(self):
          Start_address =   self.textEdit_2.toPlainText()
          How_many =   self.textEdit_3.toPlainText()
          #How_many =   self.textEdit_4.toPlainText()
          if How_many.isdigit() & Start_address.isdigit():
               print(Start_address)
               print(How_many)
               Command_Mode = self.comboBox_2.currentText()
               #print(Command_Mode)
               if(Command_Mode == "RR"):
                    #print(str(hex(int(Start_address))))
                    hex_number = hex(int(Start_address))[2:]
                    print(str(hex_number))
                    #print(len(hex_number))
                    hex_number_how_many = hex(int(How_many))[2:]
                    if(len(hex_number) == 1):
                        str_hex = "000" + str(hex_number)
                    elif(len(hex_number) == 2):
                        str_hex = "00" + str(hex_number)

                    elif(len(hex_number) == 3):
                        str_hex = "0" + str(hex_number)
                    else:
                        str_hex = str(hex_number)

                    #############################
                    if(len(hex_number_how_many) == 1):
                        str_hex_number_how_many = "000" + str(hex_number_how_many)
                    elif(len(hex_number_how_many) == 2):
                        str_hex_number_how_many = "00" + str(hex_number_how_many)

                    elif(len(hex_number_how_many) == 3):
                        str_hex_number_how_many = "0" + str(hex_number_how_many)
                    else:
                        str_hex_number_how_many = str(hex_number_how_many)

                    Command = "@"+  self.textEdit.toPlainText()+"RR" + str_hex + str_hex_number_how_many
                    my_instance = CheckSum()
                    checksum = my_instance.CheckSum(Command)
                    #print(Command + checksum+ "*")
                    query = Command + checksum+ "*"
                    self.textEdit_4.setText(checksum)
                    self.textEdit_5.setText(query)

                         
                         
               elif(Command_Mode == "RW"):
                    print("")
   
               else:
                    print("")


          else:
            print("The string does not represent an integer")
            # create a message box
            msg_box = QMessageBox()
            msg_box.setText("Start address could not be blank and the how many channel section could not be blank and all must be integers")
            msg_box.setWindowTitle("Error")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setStandardButtons(QMessageBox.Ok)

            # show the message box and wait for the user to close it
            msg_box.exec_()

            # show a message box
            #messagebox.showinfo("Info", "The start address must be integer and the how many section could not be blank and must be integer")

            # run the event loop

       

    def refresh(self):
         
          with open("response.txt", "r") as file:
            file_contents = file.readline().strip()

            #address_called = first_line[5:9]
            #print(address_called)
            #print(file_contents)

            self.textBrowser.setText(file_contents)

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
               message = self.textEdit_5.toPlainText().encode()


               ser.write(message)
               with open('sending.txt', 'w') as file:
                   file.write(message.decode())
               ser.close()
               time.sleep(3)
               with open("response.txt", "r") as file:
                    file_contents = file.readline().strip()

               #address_called = first_line[5:9]
               #print(address_called)
               #print(file_contents)
               self.textBrowser.setText(file_contents)


           elif(PLC_Type == "Delta PLC"):
              print("Delta PLC")
           else:
                print("Error")



    def exit_program(self):
          exit()

      
 
class CheckSum:
     def CheckSum(self, input_data):
        my_array = []
        my_hex_array = []
        first_character_list = []
        second_character_list = []


        for i in range(len(input_data)):
            my_array.append(input_data[i])
            my_hex_array.append(bytes(input_data[i],"utf-8").hex())
    


        for string in my_hex_array:
            first_digit = string[0]
            first_character_list.append(int(first_digit))

        for string in my_hex_array:
            first_digit = string[1]
            second_character_list.append(int(first_digit))

        first_binary_list = [bin(num)[2:].zfill(4) for num in first_character_list]


        second_binary_list = [bin(num)[2:].zfill(4) for num in second_character_list]
  

        result = int(first_binary_list[0], 2)  # convert first element to int
        for i in range(1, len(first_binary_list)):
            num = int(first_binary_list[i], 2)  # convert next element to int
            result ^= num  # perform XOR operation

        binary_result = bin(result)[2:].zfill(len(first_binary_list[0]))  # convert result back to binary
        #print(binary_result)  # output: 0010 1110 1110 0011
        decimal_value = int(binary_result, 2)
        #print(decimal_value)  # Output: 42

        ###############################33
        result_2 = int(second_binary_list[0], 2)  # convert first element to int
        for i in range(1, len(second_binary_list)):
           num_2 = int(second_binary_list[i], 2)  # convert next element to int
           result_2 ^= num_2  # perform XOR operation

        binary_result_2 = bin(result_2)[2:].zfill(len(second_binary_list[0]))  # convert result back to binary
        #print(binary_result_2)  # output: 0010 1110 1110 0011

        decimal_value_2 = int(binary_result_2, 2)
        #print(decimal_value_2)  # Output: 42

        #print("Check Sum: " + str(decimal_value) + str(decimal_value_2))
        if(decimal_value == 10):
           decimal_value = "A"
        elif(decimal_value == 11):
           decimal_value = "B"
        elif(decimal_value == 12):
           decimal_value = "C"
        elif(decimal_value == 13):
           decimal_value = "D"
        elif(decimal_value == 14):
           decimal_value = "D"
        elif(decimal_value == 15):
           decimal_value = "F"
        else:
           decimal_value = decimal_value

        if(decimal_value_2 == 10):
           decimal_value_2 = "A"
        elif(decimal_value_2 == 11):
           decimal_value_2 = "B"
        elif(decimal_value_2 == 12):
           decimal_value_2 = "C"
        elif(decimal_value_2== 13):
           decimal_value_2 = "D"
        elif(decimal_value_2 == 14):
           decimal_value_2 = "D"
        elif(decimal_value_2 == 15):
           decimal_value_2 = "F"
        else:
           decimal_value_2 = decimal_value_2

        #print("Final C-Command: " + input_data + str(decimal_value) + str(decimal_value_2) + "*")
        return str(decimal_value) + str(decimal_value_2)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


