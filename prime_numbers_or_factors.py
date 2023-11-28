# let us check whether a number is prime or not using nested for loops
# A prime number is a natural number that has exactly two numbers: 1 and itself
# n will take the values from 2 to 9 one by one
# x will take values from 2 to n - 1
# for each value of x, we check  if n % x is equal to 0
# if condition is true the print statement is executed
# then we break out of the inner loop
# if n is 6 and x is 2, the print statement ie line  wll be exceuted.
# the program will not check for other values.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
