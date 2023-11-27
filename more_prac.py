# .format method manually specifying the interpolation order
age = 30
name = "Alicia"

# Using numeric indices
print("Hello {1}! Are you {0} years old?".format(age, name))

# Use keyword arguments
print("Hello {name}! Are you {age} years old today?".format(name="Alicia", age=30))
