#!/usr/bin/python3
import sys


def example():
    assert ("windows" in sys.platform), "This code can only run on Windows."
    with open('ex6.py') as ex:
        bbytes = ex.read()
        print(bbytes)


if __name__ == '__main__':
    try:
        example()
    except AssertionError as E:
        print(E)
        print("Could not run file.")
    except FileNotFoundError as A:
        print(A)
        print("File does not exist.")
