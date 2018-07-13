import urllib.request
import cv2
import numpy as np

#
class stream:

    def __init__(self, url):
        self.url = url
        self.instance = urllib.request.urlopen(self.url)
        self.bytes = bytes()

    def getFrame(self):
        self.bytes += self.instance.read(1024)
        self.a = self.bytes.find(b'\xff\xd8')
        self.b = self.bytes.find(b'\xff\xd9')
        if self.a!=-1 and self.b!=-1:
            self.jpg = bytes[a:b+2]
            self.bytes= bytes[b+2:]
            self.frame = cv2.imdecode(np.fromstring(self.jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
            return self.frame
        else:
            pass

# def __init__ (url):
#     global instance, bytes
#     instance = urllib.request.urlopen(url)
#     bytes=bytes()
#
# def getFrame():
#     bytes += instance.read(1024)
#     a = bytes.find(b'\xff\xd8')
#     b = bytes.find(b'\xff\xd9')
#     if a != -1 and b != -1:
#         jpg = bytes[a:b+2]
#         bytes = bytes[b+2:]
#         frame = frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
#         return frame
