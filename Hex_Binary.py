# Assume Response
# 00000000000000
hex_string = '00000000000000'

binary_list = []
for hex_char in hex_string:
    binary_string = bin(int(hex_char, 16))[2:].zfill(4)
    binary_list.append(binary_string)

print(binary_list)