import serial
from time import sleep
#
# ser = serial.Serial(
#     port = "COM3",
#     baudrate = 38400
#     # baudrate = 115200,
#     # stopbits = serial.STOPBITS_ONE
# )


with serial.Serial("COM3", 115200, timeout = 1) as ser:


    print(ser.isOpen())

    ledOn = "\x7e\xff"
    # ledOn1 = ""
    ledOff = "\x7e\x00"
    # ledOff1 = ""
    # ledOn = "\xff"
    # ledOff = "\x00"
    # ser.readTimeout = 1
    ser.write(ledOn)
    # readOne = ser.read(100)
    sleep(1)
    ser.write(ledOff)
    readTwo = ser.readline()
    # print(readOne)
    print(readTwo)

    ser.close()
