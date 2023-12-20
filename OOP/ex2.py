#!/usr/bin/python3
# let us bind the function hi to class attribute say hi
def hi(obj):
    print("Hello, my name is " + obj.name + ".")

class Robot:
    say_hi = hi


x = Robot()
x.name = 'Makena'
Robot.say_hi(x)
