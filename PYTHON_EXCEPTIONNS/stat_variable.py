#!/usr/bin/python3
class Dog:
    # if you craete a field outside of any other methods,
    # it is automatically a static variable
    # its value is shared by every object of type dog that is ever created
    # this static variable "number" will keep track of all Dog objects

    number = 0

    # let us initialze our dog object
    def __init__(self, name="Unknown"):
        # assignment
        self.name = name
        # if you want to reference a static variable
        # precede with the class name
        Dog.number += 1

    @staticmethod
    def GetNumberOfDogObjects():
        print("{}".format(Dog.number))


def main():
    Pickels = Dog("Pickles")
    Bones = Dog("Bones")
    Buster = Dog("Buster")
    Bones.GetNumberOfDogObjects()
    Buster.GetNumberOfDogObjects()


main()
