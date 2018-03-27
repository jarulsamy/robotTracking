
import socket
from threading import Thread
from myro import *
import time
init("COM4")


setLED("Left", "off")
setLED("Right", "off")
setLED("Front", "off")
setLED("Back", "off")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PORT = 10000
PORT = 10000
HOST = '127.0.0.1'

serversocket.bind((HOST, PORT))
serversocket.listen(10)
# 4096
MAX_LENGTH = 1024

def handle(clientsocket):
  while 1:
    buf = clientsocket.recv(MAX_LENGTH)
    try:
        exec(buf)
        time.sleep(.001)
    except Exception:
        print("Ur command errored!!!", buf)
    print buf

    if buf == '':
        return #client terminated connection

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()

    ct = Thread(target=handle, args=(clientsocket,))
    ct.run()
