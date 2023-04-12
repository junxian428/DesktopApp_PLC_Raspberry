import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,   bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

# send data over serial communication
ser.write(b'@10RR000400084D*\r')


while True:
    data = ser.read(1)
    if data:
        print(data)