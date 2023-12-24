#!/usr/bin/python3
# let us rewrite the class instead using a public attribute
# just to illustarate difference between using getters and setters
# to acess private attributes and how we can directly access public
# attributes

class P:
    def __init__(self, x):
        self.x = x


def main():
    p1 = P(10)
    p2 = P(5)
    print(p1.x + p2.x)


main()
