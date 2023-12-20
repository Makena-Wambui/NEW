#!/usr/bin/python3
def f(x):
    f.counter = getattr(f, 'counter', 0) + 1


if __name__ == '__main__':
    for i in range(10):
        f(i)
    print(f.counter)
    print(f.__dict__)
