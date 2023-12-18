#!/usr/bin/python3

class Sum:
    @staticmethod
    def Getsum(*args):
        sum = 0
        # let us find the sum of all values passed to this method
        for number in args:
            sum = sum + number
        return sum


def main():
    print("Sum is: {:d}".format(Sum.Getsum(1, 2, 3, 4)))


main()
