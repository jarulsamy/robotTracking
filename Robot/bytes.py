import serial
from time import sleep


with serial.Serial("COM4", 115200, timeout = 1) as ser:
    def sendCommand(command):
        forward ='\x6d\xc8\xc8\x00\x00\x00\x00\x00\x00'
        stop ='\x6d\x64\x64\x00\x00\x00\x00\x00\x00'
        zero = '\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        ser.write(forward)
        ser.read(10)
        sleep(1)
        ser.write(zero)
        ser.read(10)
        ser.write(stop)
        ser.read(10)
        sleep(1)

    sendCommand('foo')
