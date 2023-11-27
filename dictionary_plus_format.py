# Using dictionaries with the format method
# use the dictionary unpacking operator **
person = {"name": "Alicia", 'age': 30}

print("Hello {name}. You are {age} years old.".format(**person))
