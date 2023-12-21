#!/usr/bin/python3
class Robot:
    def hi(self):
        print("my name is " + self.name + "!")


x = Robot()
x.name = "Makena"
print(x.name)
x.hi()
