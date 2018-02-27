import sys
import serial
import socket

HOST = '127.0.0.1'
PORT = 10000
s = socket.socket()
s.connect((HOST, PORT))


s.send('turnLeft(1,1)')
