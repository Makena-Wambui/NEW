#!/usr/bin/python3
import sys


def windo():
    assert ("windows" in sys.platform), "THis function can only run on Windows."


if __name__ == '__main__':
    try:
        windo()
    except AssertionError as Err:
        print(Err)
        print("Function only executed on Windows")
    else:
        print("In the absence of exceptions, print this.")
    finally:
        print("Whether there are exceptions or not, this will always run")
