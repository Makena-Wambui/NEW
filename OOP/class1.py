#!/usr/bin/python3
class Robot:
    pass


if __name__ == '__main__':
    # lets create two instances of the class Robot and store
    # them in the variables x and y
    x = Robot()
    y = Robot()
    # let us create an alias for y
    y2 = y
    print(y2 == y)
    print(y2 == x)
