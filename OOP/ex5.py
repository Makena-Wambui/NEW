#!/usr/bin/python3
class Robot:  # let us define a class Robot
    # init is the constructor method in Python.
    # it will be automatically called when an
    # instance of the class is created.
    # init takes two parameters.
    # self which represents an instance of the class.
    # name whose default value is None.
    # inside init we set an instance variable self.name
    # to the value of the name parameter.

    def __init__(self, name=None):
        self.name = name
    # we define another method say_hi
    # takes the parameter self.
    # this will enable it to access the instance variables of the class.
    # then check whether the name attribute is set for the instance

    def say_hi(self):
        if self.name:
            print("Hello i am {}".format(self.name))
        else:
            print("I am a robot without a name.")


# let us now create instances of the class
# and store them in the variables x and y
x = Robot()
x.say_hi()
# i did not provide a name argument during the creation of
# x instance so init will set name param ie self.name to default
# value of None.
y = Robot('Marvin')
y.say_hi()
