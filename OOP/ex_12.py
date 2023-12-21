#!/usr/bin/python3

from typesofattributes import A

if __name__ == '__main__':
    x = A()
    print(x.pub)
    print("{:s} My value can be changed.".format(x.pub))
    print("{}".format(x._prot))
    print("{}".format(x.__priv))
