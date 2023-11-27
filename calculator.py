'''
Lets build a calculator
I want user to enter two integers and an operator like this: 5 + 4
I will be using input and split
'''
num1, operator, num2 = input('Enter calculation: ').split()

# Convert the strings(numbers only) to integers
num1 = int(num1)
num2 = int(num2)

# Perform the calculation based on the operator entered.
if operator == '+':
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == '-':
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == '*':
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == '/':
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == '%':
    print("{} % {} = {}".format(num1, num2, num1 % num2))
# If operator entered is none of the above
else:
    print('Invalid operator.')
