# https://github.com/junxian428/ASCII_HEX_BINARY_XOR_Checksum_Calculation_Script/blob/main/Main.py
# Tools From Junxian428

user_input = input("C-Command : ")
#@10RR00040003
Character_Length = len(user_input)
print("\n")
print(" Character : " + user_input + " Character Length : " + str(Character_Length))

def Assign(input_data):
    my_array = []
    my_hex_array = []
    first_character_list = []
    second_character_list = []


    for i in range(len(input_data)):
        my_array.append(input_data[i])
        my_hex_array.append(bytes(input_data[i],"utf-8").hex())
    
    print(my_array)
    print(my_hex_array)

    for string in my_hex_array:
        first_digit = string[0]
        first_character_list.append(int(first_digit))

    for string in my_hex_array:
        first_digit = string[1]
        second_character_list.append(int(first_digit))

    print("First Row (Hex)" + str(first_character_list))
    print("Second Row (Hex)" + str(second_character_list))

    first_binary_list = [bin(num)[2:].zfill(4) for num in first_character_list]
    print("First Row (Binary): " + str(first_binary_list))

    second_binary_list = [bin(num)[2:].zfill(4) for num in second_character_list]
    print("Second Row (Binary): "  + str(second_binary_list))

    ###############################3

    result = int(first_binary_list[0], 2)  # convert first element to int
    for i in range(1, len(first_binary_list)):
        num = int(first_binary_list[i], 2)  # convert next element to int
        result ^= num  # perform XOR operation

    binary_result = bin(result)[2:].zfill(len(first_binary_list[0]))  # convert result back to binary
    print(binary_result)  # output: 0010 1110 1110 0011
    decimal_value = int(binary_result, 2)
    print(decimal_value)  # Output: 42

    ###############################33
    result_2 = int(second_binary_list[0], 2)  # convert first element to int
    for i in range(1, len(second_binary_list)):
        num_2 = int(second_binary_list[i], 2)  # convert next element to int
        result_2 ^= num_2  # perform XOR operation

    binary_result_2 = bin(result_2)[2:].zfill(len(second_binary_list[0]))  # convert result back to binary
    print(binary_result_2)  # output: 0010 1110 1110 0011

    decimal_value_2 = int(binary_result_2, 2)
    print(decimal_value_2)  # Output: 42

    print("Check Sum: " + str(decimal_value) + str(decimal_value_2))
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

    print("Final C-Command: " + input_data + str(decimal_value) + str(decimal_value_2) + "*")


    ###################################


Assign(user_input)