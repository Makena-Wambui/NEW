#!/usr/bin/python3
import sys


def lin():
    assert ("windows" in sys.platform), "This code only runs on windows."


if __name__ == '__main__':
    try:
        lin()
    except AssertionError as E:
        print("Exception error: {} captured.".format(E))
    else:
        try:
            with open('exxx.py') as file:
                bbytes = file.read()
                print(bbytes)
        except FileNotFoundError as F:
            print(F)
