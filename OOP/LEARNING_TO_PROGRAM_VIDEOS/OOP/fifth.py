#!/usr/bin/python3
class Coordinate:
    """This Coordinate class defines a coordinate on a 2d plane
    with x and y values."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # now let us create a method that finds the distance between two coordinates.
    def distance(self, other):
        """This method returns distance between two coordinates."""
        x_diff_squared = (self.x - other.x) ** 2
        y_diff_squared = (self.y - other.y) ** 2
        distance = (x_diff_squared + y_diff_squared) ** 0.5
        return distance
    # let us define another magic method __str__
    # so we dont get the weird uninformative value when we try to print an object.
    def __str__(self):
        return "Coordinate (" + str(self.x) + ", " + str(self.y) + ")"


def main():
    coord_1 = Coordinate(3, 4)
    coord_2 = Coordinate(0, 0)
    print(coord_1)
    print(coord_1.x)
    print(coord_2.y)
    print(coord_1.distance(coord_2))


main()
# help(Coordinate)
