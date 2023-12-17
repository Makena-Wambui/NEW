#!/usr/bin/python3
import sys


def linux_interaction():
    assert ("linux" in sys.platform), "This code only runs on Linux."
    print("Hello Makena.")


if __name__ == '__main__':
    linux_interaction()
