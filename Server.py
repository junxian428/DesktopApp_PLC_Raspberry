import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

# send data over serial communication
ser.write(b'@10RR000400084D*\r')


while True:
    data = ser.readline()
    if data:
        #print("Byte Data Replied from PLC: " + data)
        data_removed = data[5:]
        s_str = data.decode('utf-8')
        print(s_str)
        data_removed_byte = data_removed.decode('utf-8')
        print("After removed: " + data_removed_byte) 
        response_code = data[5:7].decode('utf-8')
        print("___________________________________________")
        print("Response Code : " + response_code)
        mode = data[3:5].decode('utf-8')
        print("Data mode : " + mode)
        if response_code == "00":
            print("Response: Normal Completion")
            if(mode == "RR"):
                print("CIO AREA READ")
            elif(mode == "RL"):
                print("LR AREA READ")
            elif(mode == "RH"):
                print("HR AREA READ")
            elif(mode == "RH"):
                print("HR AREA READ")
            else:
                print("Invalid Mode")

        elif response_code =="01":
            print("Not Executable in RUN mode")

        elif response_code =="02":
            print("Not Executable in MONITOR mode")

        elif response_code =="03":
            print("UM write-protected")

        elif response_code == "04":
            print("Address over")

        elif response_code == "0B":
            print("Not executable in PROGRAM mode")

        elif response_code =="13":
            print("FCS error")

        elif response_code =="14":
            print("Format error")

        elif response_code =="15":
            print("Entry number data error")

        
        else:
            print("Uncaught Error")
    


