#!/usr/bin/python3
def div():
    num1, num2 = input("Enter your two numbers: ").split()
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))


try:
    div()
except ZeroDivisionError as Err:
    print(Err)
except TypeError as Type:
    print(Type)
else:
    print("Print in absence of exceptions.")
finally:
    print("Execute no matter what.")
