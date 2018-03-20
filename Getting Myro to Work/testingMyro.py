### Testing Myro ###
sys.path.insert(0, 'C:\Python27\myro') # No Longer used # Now using pipeline to python 2.4
from myro import *

init("COM7")

forward(1,1)
wait(1)
stop()
print('foo')
