#!/usr/bin/python3

class USER:
    pass

user1 = USER()
# user1 is an instance of the USER class.
# or user1 is an object.
# now let us attach data to this object
user1.first_name = "Dave"
user1.last_name = "Smith"
# first_name and last_name are attached to the object.
# they are called fields.
# fields are data attached to an object
# they store data related to a specific object.
print(user1.first_name, user1.last_name)
# names of fields should not be capitalized.
# and if you use more than one word as the field name,
# separate them with underscores. 
# improve readability.
user2 = USER()
user2.first_name = "Alicia"
user2.last_name = "Makena"
first_name = "Jake"
last_name = "Tendai"
user1.age = 30
user2.favorite_book = "The Alchemist"
print(user2.first_name, user2.last_name)
print(first_name, last_name)
print(user1.age)
# print(user2.age) will give attribute error because this object does not have this specific attribute.
