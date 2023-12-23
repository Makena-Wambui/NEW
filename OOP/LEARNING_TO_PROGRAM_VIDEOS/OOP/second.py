#!/usr/bin/python3
class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # let us define a getter method.
    # @property allows us to refer to each of the individual attributes.
    @property
    def height(self):
        print("Retrieving Height attribute..")
        return (self.__height)

    # let us now define our setter method
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter a valid value.")

    @property
    def width(self):
        print('Retrieving Width..')
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Enter a valid value.")

    def Get_Area(self):
        return int(self.__width) * int(self.__height)


def main():
    a = Square()
    height = input("Enter the height: ")
    width = input("Enter the width: ")
    a.height = height
    a.width = width
    print("Height: {}".format(a.height))
    print("Width: {}".format(a.width))
    print("The area is: {}".format(a.Get_Area()))


if __name__ == '__main__':
    main()
