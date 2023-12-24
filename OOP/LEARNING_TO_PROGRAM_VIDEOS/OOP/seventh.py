#!/usr/bin/python3
# let us design a class with getters and setters to encapsulate the private attribute self.__x
class P:
    def __init__(self, x):
        self.__x = x

    def Get_X(self):
        return self.__x

    def Set_X(self, value):
        self.__x = value

    def __str__(self):
        return "P(" + str(self.__x) + ")"


def main():
    p1 = P(10)
    p2 = P(5)
    print(p1.Get_X())
    p1.Set_X(8)
    print(p1.Get_X())
    print(p1)
    p1.Set_X(p1.Get_X() + p2.Get_X())
    print(p1.Get_X())


main()
