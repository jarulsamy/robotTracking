### Testing Myro ###

import sys
sys.path.insert(0, 'C:\Python27\myro')
from myro import *

init("COM7")

forward(1,1)
wait(1)
stop()
print('foo')
