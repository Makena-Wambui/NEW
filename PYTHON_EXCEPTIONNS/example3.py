#!/usr/bin/python3
import sys


def linux_interaction():
    assert ('windows' in sys.platform), "This code can only run on Windows."
    print("Hello Makena.")


if __name__ == '__main__':
    try:
        linux_interaction()
    except:
        print("Function not executed on Linux")
