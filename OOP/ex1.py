#!/usr/bin/python3
def hi(obj):
    print("Hi, My name is " + obj.name + "!")


class Robot:
    pass


x = Robot()
x.name = 'Makena'
hi(x)
