#!/usr/bin/python3
# let us create extra attributes.
class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("I am an instance of the Robot class.My name is {}".format(self.name))
        else:
            print("I do not have a name yet.")
        if self.build_year:
            print("I was built in {}".format(self.build_year))
        else:
            print("I do not know my build year.")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, year):
        self.build_year = year

    def get_build_year(self):
        return self.build_year


x = Robot("Titus", 2016)
y = Robot()
y.set_name("Ares")
x.say_hi()
y.say_hi()
