#!/usr/bin/python3
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


# This code generate the Fibonacci series up to a certain number n
# Fibonacci series is a sequence of numbers starting from 0 and 1
# Where each number is a sum of the two previous numbers
# First 10 numbers in the Fibonacci series are: 0,1, 1, 2, 3, 5,..
# The second function, fib2(n), returns the Fibonacci series up to n as a list
def fib2(n):
    list = []
    a, b = 0, 1
    while a < n:
        list.append(a)
        a, b = b, a + b
    return list
