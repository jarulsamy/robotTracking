### Learning Classes ###

import sys

class robotTracking(object):
# Variables defined here can be used when the class is called with that given name.
# In this case math = robotTracking() so for example, print(math.newThing)
    newThing = 0
    def __init__(self):
        print('New way to do Math!')
        print('Made by Joshua Arulsamy')
    def add2Things(self, a, b):
        self.newThing = a + b
        self.thing = b
        return self.thing
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
foo = math.add2Things(2, 3)
print(foo)
