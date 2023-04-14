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



class Ui(QtWidgets.QMainWindow):

    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('UI/COMM.ui', self) # Load the .ui file

          self.setWindowTitle('PLC Raspberry Pi')
          #combo_box = self.findChild(QComboBox, "comboBox")
          #combo_box.currentIndexChanged.connect(self.selectionChanged)
          self.textEdit.setText("10")
          self.textEdit_2.setText("4.01")
          #global str_total
          #global Key_Array
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
          self.button.clicked.connect(self.printValue)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
          self.button.clicked.connect(self.exit_program)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          self.button.clicked.connect(self.generate_checksum_query)
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
          self.button.clicked.connect(self.refresh)
          self.textBrowser.setText("Waiting for response...")
          self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
          self.button.clicked.connect(self.generate_hex)


          # connect the currentIndexChanged() signal of the ComboBox to our custom slot
          self.comboBox_6.currentIndexChanged.connect(self.on_combobox_select)

          self.show() # Show the GUI
    def generate_hex(self):
          print("hex")
          bit_0 = self.textEdit_8.toPlainText()
          bit_1 = self.textEdit_9.toPlainText()
          bit_2 = self.textEdit_10.toPlainText()
          bit_3 = self.textEdit_11.toPlainText()

          Group1 = bit_0 + bit_1 + bit_2 + bit_3 

          bit_4 = self.textEdit_12.toPlainText()
          bit_5 = self.textEdit_13.toPlainText()
          bit_6 = self.textEdit_14.toPlainText()
          bit_7 = self.textEdit_15.toPlainText()
                    
                    
          Group2 = bit_4 + bit_5 + bit_6+ bit_7


          bit_8 = self.textEdit_16.toPlainText()
          bit_9 = self.textEdit_17.toPlainText()
          bit_10= self.textEdit_18.toPlainText()
          bit_11 = self.textEdit_19.toPlainText()

          Group3 = bit_8 + bit_9 + bit_10 + bit_11 


          bit_12 = self.textEdit_20.toPlainText()
          bit_13 = self.textEdit_21.toPlainText()
          bit_14 = self.textEdit_22.toPlainText()
          bit_15 = self.textEdit_23.toPlainText()

          Group4 = bit_12 + bit_13 + bit_14 + bit_15
         #A = int(Group1, 2)
         # B = int(Group2, 2)
         # C = int(Group3, 2)
          #D = int(Group4, 2)

         # print(bin(A) + " " + bin(B) + " " +  bin(C) + " ")
          print(Group1 + " "+ Group2  + " "+ Group3 +" " +Group4)

    def on_combobox_select(self):
          print("Selected key:")
          # get the current index of the ComboBox
          current_index = self.comboBox_6.currentIndex()

          # print the current index to the console
          print("Current index:", current_index)
          print("Current Key: " + str(Key[current_index]))
          #print(Key_Array[Key[current_index]])
          # assign the values to the text edit widgets
          list_array = Key_Array[Key[current_index]]
          print(list_array)
          #reversed_list = reverse()
          self.textEdit_8.setText(list_array[3][3])
          self.textEdit_9.setText(list_array[3][2])
          self.textEdit_10.setText(list_array[3][1])
          self.textEdit_11.setText(list_array[3][0])
          self.textEdit_12.setText(list_array[2][3])
          self.textEdit_13.setText(list_array[2][2])
          self.textEdit_14.setText(list_array[2][1])
          self.textEdit_15.setText(list_array[2][0])
          self.textEdit_16.setText(list_array[1][3])
          self.textEdit_17.setText(list_array[1][2])
          self.textEdit_18.setText(list_array[1][1])
          self.textEdit_19.setText(list_array[1][0])
          self.textEdit_20.setText(list_array[0][3])
          self.textEdit_21.setText(list_array[0][2])
          self.textEdit_22.setText(list_array[0][1])
          self.textEdit_23.setText(list_array[0][0])
        ###################################

    def generate_checksum_query(self):
          Start_address =   self.textEdit_2.toPlainText()
          How_many =   self.textEdit_3.toPlainText()
          #How_many =   self.textEdit_4.toPlainText()
          if How_many.isdigit() & Start_address.isdigit():
               #print(Start_address)
               #print(How_many)
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
            #my_instance = CheckSum()
            #checksum = my_instance.CheckSum(Command)
            my_instance = CheckSum()
            refreshdata = my_instance.response_hex_binary()
            keys_list = list(refreshdata.keys())
            global Key_Array
            global Key
            Key_Array = refreshdata
            Key = keys_list
            print(keys_list)
            self.comboBox_6.clear()
            self.comboBox_7.clear()

            for key in keys_list:
               self.comboBox_6.addItem(str(key))
               self.comboBox_7.addItem(str(key))

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
     
     def response_hex_binary(self):
        #print("Hello")


        #data = ser.readline()
        with open('sending.txt', 'r') as file:
            first_line = file.readline().strip()


        with open('response.txt', 'r') as file:
            data = file.readline().strip()

        print("Sending C-command: " + first_line)
        address_called = first_line[5:9]
        number_start_address = int(address_called)
        print("Address is called start from :" + str(number_start_address))
        #print(CheckSum("@10RR00040008"))
        #print("Byte Data Replied from PLC: " + data)
        data_removed = data[5:]
        s_str = data
        #with open('response.txt', 'w') as file:
        #    file.write(s_str)
        
        #print("PLC response : " + s_str)
        #print("After removed: " + data_removed_byte) 
        # Response CheckSum 
        #print("______________________________________")
        #return_checksum = data[len(data)-4:len(data)-2]
        #print("Response Check Sum: " + return_checksum)
        #Calculation CheckSum
        calculation_checksum = s_str[:len(s_str)-4]
        #print("The input for checksum : " + str(calculation_checksum))
        #CheckSum_Result = CheckSum(calculation_checksum)
        #print("CheckSum : " + CheckSum_Result)
        ########################################
        #Compare the received checksum and calculated checksum
        #if(return_checksum == CheckSum_Result):
        #    print("PLC -> Raspberry Pi. No CheckSum Error. Can proceed")
        #else:
        #    print("PLC -> Raspberry Pi. There is checksum error")
        ########################################
        response_code = data[5:7]
        #print("___________________________________________")
        #print("Response Code : " + response_code)
        mode = data[3:5]
        print("Data mode : " + mode)
        if response_code == "00":
            print("Response: Normal Completion")
            ############################## Do the address operation
            Address_Operation = data[7:len(data)-3]
            print("What is this" + Address_Operation)
            print("Total Length address returned : " + str(len(calculation_checksum)))
            print("Total Bits " + str(len(Address_Operation) * 4))
            number_channel = len(Address_Operation) / 4
            print("1 Channel = 4. That's reason why N address / 4 = N channel: " + str(number_channel))

            ##############################
            binary_list = []
            for hex_char in Address_Operation:
                binary_string = bin(int(hex_char, 16))[2:].zfill(4)
                binary_list.append(binary_string)

            print(binary_list)
            # One group = One channel = 15 bytes
            grouped_list = [binary_list[i:i+4] for i in range(0, len(binary_list), 4)]

            print(grouped_list)
            grouped_list_len = len(grouped_list)
            print("Group list element : " + str(len(grouped_list)))

            result_dict = {}
            key = number_start_address

            for lst in grouped_list:
                result_dict[key] = lst
                key += 1

            return result_dict
            #result_dict[5][2] = "0100"
            #result_dict[5][1] = "1100"
            #print(result_dict)
            #keys_list = list(result_dict.keys())
            #print(keys_list)
            #for key in my_dict.keys():
            #    self.combo_box.addItem(str(key))

            #user_select_channel = 0
            #index = 0

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


