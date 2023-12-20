#!/usr/bin/python3
class Robot:
    pass

# please note this is not the way to properly craete instance attributes.
# this is just for practoce.
x = Robot()
y = Robot()
y2 = y
x.name = 'Jake'
x.build = 1996
y2.name = 'Melody'
y2.build = 2004
print("{}".format(x.name))
print("{}".format(y2.build))
