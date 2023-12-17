#!/usr/bin/python3
def openn():
    with open('ex.py') as ex:
        read_bytes = ex.read(50)
        print(read_bytes)


if __name__ == '__main__':
    try:
        openn()
    except FileNotFoundError as err:
        print(err)
        print("Could not open file.")
