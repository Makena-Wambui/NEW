#!/usr/bin/python3
class Robot(object):
    pass

try:
    x = Robot()
    y = Robot()
    Robot.name = 'Zeus'
    print(Robot.name)
    print(x.name)
    print(y.name)
    print(x.__dict__)
    print(y.__dict__)
    print(Robot.__dict__)
    print(x.age)
except AttributeError as Err:
    print(Err)
print(getattr(y, 'age', 100))
