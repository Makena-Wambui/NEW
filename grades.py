# If age is 5, go to Kindergarten.
age = eval(input('Enter your age: '))
if age < 5:
    print('Still a baby')
elif age == 5:
    print('Welcome to Kindergarten')
# Age 6 to 17, go to grade 1 to 12.
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("You are in grade {}".format(grade))
# If age is greater than 17, go to college
else:
    print('Time for college!')
