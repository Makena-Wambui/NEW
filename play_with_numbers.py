'''
Ask for input from the user, num1 and num2
Utilize the input function
And the input function which will split the two values if there is
a whitespace between them
'''
num1, num2 = input('Enter your values: ').split()

# Convert num1 and num2 which are strings into integers
num1 = int(num1)
num2 = int(num2)

# Add num1 and num2 and store in a variable total
total = num1 + num2

# Subtract and store in variable called sub
sub = num1 - num2

# Multiply and store in a variable called mult
mult = num1 * num2

# Divide and store in div
div = num1 / num2

# Floor division
Div = num1 // num2

# Calculate modulus and store in a variable called rem
rem = num1 % num2

# Print your results
print("{} + {} = {}".format(num1, num2, total))

print("{} - {} = {}".format(num1, num2, sub))

print("{} * {} = {}".format(num1, num2, mult))

print("{} / {} = {}".format(num1, num2, div))

print("{} // {} = {}".format(num1, num2, Div))

print("{} % {} = {}".format(num1, num2, rem))
