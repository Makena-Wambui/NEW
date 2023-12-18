#!/usr/bin/python3
import sys


def linuxxx():
    assert ("linux" in sys.platform), "This code can only run on Linux."


if __name__ == "__main__":
    try:
        linuxxx()
    except AssertionError as E:
        print(E)
    else:
        print("Hello Mama Jake.")
