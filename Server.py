import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

# send data over serial communication
# ser.write(b'@10RR000400084D*\r')

def CheckSum(input_data):
    my_array = []
    my_hex_array = []
    first_character_list = []
    second_character_list = []


    for i in range(len(input_data)):
        my_array.append(input_data[i])
        my_hex_array.append(bytes(input_data[i],"utf-8").hex())
    
    #print(my_array)
    #print(my_hex_array)

    for string in my_hex_array:
        first_digit = string[0]
        first_character_list.append(int(first_digit))

    for string in my_hex_array:
        first_digit = string[1]
        second_character_list.append(int(first_digit))

    #print("First Row (Hex)" + str(first_character_list))
    #print("Second Row (Hex)" + str(second_character_list))

    first_binary_list = [bin(num)[2:].zfill(4) for num in first_character_list]
    #print("First Row (Binary): " + str(first_binary_list))

    second_binary_list = [bin(num)[2:].zfill(4) for num in second_character_list]
    #print("Second Row (Binary): "  + str(second_binary_list))

    ###############################3

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

    ###################################


while True:
    # prompt user for input
    #user_input = input("Enter data to send (type 'exit' to quit): ")

    # check if user entered the exit command
    #if user_input == 'exit':
        #break
    #ser.write(user_input.encode())
    # convert user input to bytes and send over serial
    #ser.write(user_input.encode())

    data = ser.readline()
    if data:
        with open('sending.txt', 'r') as file:
            first_line = file.readline().strip()

        print("Sending C-command: " + first_line)
        address_called = first_line[5:9]
        number_start_address = int(address_called)
        print("Address is called start from :" + str(number_start_address))
        #print(CheckSum("@10RR00040008"))
        #print("Byte Data Replied from PLC: " + data)
        data_removed = data[5:]
        s_str = data.decode('utf-8') # @10RR0000000000000041*
        with open('response.txt', 'w') as file:
            file.write(s_str)
        
        print("PLC response : " + s_str)
        data_removed_byte = data_removed.decode('utf-8')
        #print("After removed: " + data_removed_byte) 
        # Response CheckSum 
        print("______________________________________")
        return_checksum = data_removed_byte[len(data_removed_byte)-4:len(data_removed_byte)-2]
        print("Response Check Sum: " + return_checksum)
        #Calculation CheckSum
        calculation_checksum = s_str[:len(s_str)-4]
        print("The input for checksum : " + str(calculation_checksum))
        CheckSum_Result = CheckSum(calculation_checksum)
        print("CheckSum : " + CheckSum_Result)
        ########################################
        #Compare the received checksum and calculated checksum
        if(return_checksum == CheckSum_Result):
            print("PLC -> Raspberry Pi. No CheckSum Error. Can proceed")
        else:
            print("PLC -> Raspberry Pi. There is checksum error")
        ########################################
        response_code = data[5:7].decode('utf-8')
        print("___________________________________________")
        print("Response Code : " + response_code)
        mode = data[3:5].decode('utf-8')
        print("Data mode : " + mode)
        if response_code == "00":
            print("Response: Normal Completion")
            ############################## Do the address operation
            Address_Operation = calculation_checksum[7:]
            print(Address_Operation)
            print("Total Length address returned : " + str(len(Address_Operation)))
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

            print(result_dict)
            #result_dict[5][2] = "0100"
            #result_dict[5][1] = "1100"
            print(result_dict)

            user_select_channel = 0
            index = 0
            #print(result_dict[user_select_channel])
            #for i in range(len(result_dict), -1, -1):
            #    for j in range(len(result_dict[user_select_channel][i])-1, -1, -1):
             #       print(f"Channel {user_select_channel}.{index}, Condition: {result_dict[user_select_channel][i][j]}")
             #       index += 1

            #print(grouped_list[0])

            ##############################
            if(mode == "RR"):
                print("CIO AREA READ")
            elif(mode == "RL"):
                print("LR AREA READ")
            elif(mode == "RH"):
                print("HR AREA READ")
            elif(mode == "RH"):
                print("HR AREA READ")
            elif(mode == "RC"):
                print("PV READ")
            elif(mode == "RG"):
                print("TC STATUS READ")
            elif(mode == "RD"):
                print("DM AREA READ")
            elif(mode == "RJ"):
                print("AR AREA READ")
            elif(mode == "RE"):
                print("EM AREA READ")
            elif(mode == "WR"):
                print("WR CIO AREA WRITE")
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

        elif response_code =="16":
            print("Command not supported")

        elif response_code =="18":
            print("Frame Length Error")


        elif response_code =="19":
            print("Not executable")

        elif response_code =="20":
            print("Could not create I/O table")

        elif response_code =="21":
            print("Not executable due to CPU unit CPU error (See notes.)")
        
        elif response_code == "23":
            print("User memory protected")

        elif response_code == "A3":
            print("Aborted due to FCS error in transmission data")

        elif response_code == "A4":
            print("Aborted due to format error in transmission data")
        
        else:
            print("Uncaught Error")
    


