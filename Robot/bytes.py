import serial
from time import sleep

ser = serial.Serial(
    port = "COM3",
    baudrate = 115200,
    stopbits = serial.STOPBITS_ONE
)


print(ser.isOpen())

ledOn = "\x7e"
ledOn1 = "\xff"
ledOff = "\x7e"
ledOff1 = "\x00"
# ledOn = "\xff"
# ledOff = "\x00"

ser.write(ledOn)
ser.write(ledOn1)
print(ser.read())
sleep(1)
ser.write(ledOff)
ser.write(ledOff1)
print(ser.read())

ser.close()
