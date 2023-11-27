'''
1 to 18 ->  Important
If 21, 50, or age > 65 -> Important
The rest: Not Important.
'''
age = eval(input('Enter your age: '))
# To convert strings automatically into integers use eval method

'''
Logical operators:
1. And: if both conditions are true, then return true.
2. Or: If either condition is true, then return true
3. Not : convert true to false and vice versa
'''
if (age >= 1) and (age <= 18):
    print('Important')
elif (age == 21) or (age == 50):
    print('Important')
elif not (age < 65):
    print('Still important')
else:
    print('Sorry, Not important')
