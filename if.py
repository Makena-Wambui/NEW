x = eval(input('Please enter an integer: '))

if x == 0:
    print("Zero")
elif x < 0:
    print('Negative integer')
elif x == 1:
    print('Single')
else:
    print(f"Number enterd is: {x:d}")
