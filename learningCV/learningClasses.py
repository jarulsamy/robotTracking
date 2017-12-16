### Learning Classes ###

import sys

class robotTracking(object):
# Variables defined here can be used when the class is called with that given name.
# In this case math = robotTracking() so for example, print(math.newThing)
    def __init__(self):
        print('foo')
        self.newThing = 'foo'
    def add2Things(self, a, b):
        self.newThing = a + b
        return self.newThing
    def sub2Things(self, a, b):
        self.newThing = a - b
        return self.newThing
    def x2Things(self, a, b):
        self.newThing = a * b
        return self.newThing
    def divide2Things(self, a, b):
        self.newThing = a / b
        return self.newThing

math = robotTracking()
print(math.sub2Things(3, 4))
print(math.newThing)
