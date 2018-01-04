### Learning Classes ###

import sys

class robotTracking(object):
# Variables defined here can be used when the class is called with that given name.
# In this case math = robotTracking() so for example, print(math.newThing)
    newThing = 0
    def __init__(self):
        print('New way to do Math!')
        print("Only Supports using 2 Numbers :P")
        print('Made by Joshua Arulsamy')
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

if len(sys.argv) != 4:
    print "Usage: Pass operation then number1 and number 2"
else:
    operation = sys.argv[1]
    num1 = sys.argv[2]
    num2 = sys.argv[3]
    # operation = str(operation)
    num1 = int(num1)
    num2 = int(num2)


if operation == 'add':
    math = robotTracking()
    foo = math.add2Things(num1, num2)
    print foo
elif operation == 'subtract':
    math = robotTracking()
    foo = math.sub2Things(num1, num2)
    print foo
elif operation == 'multiply':
    math = robotTracking()
    foo = math.x2Things(num1, num2)
    print foo
elif operation == 'divide':
    math = robotTracking()
    foo = math.divide2Things(num1, num2)
    print foo
else:
    math = robotTracking()
    print("Unsupported Operation")
