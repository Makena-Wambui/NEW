#!/usr/bin/python3
class Fraction(object):
    """This class creates that are fractions."""
    def __init__(self, numerator, denominator):
        # we use assert to declare that num and denom must be integers.
        assert type(numerator) == int and type(denominator) == int 
        self.num = numerator
        self.denom = denominator

    def __str__(self):
        """Returns the Fraction object in string format.
        """
        return "(" + str(self.num) + "/" + str(self.denom) + ")"
    
    def __add__(self,other):
        """Returns a new Fraction object after additon of self and another Fraction object.
        """
        top = (self.num * other.denom) + (self.denom * other.num)
        bottom = self.denom  * other.denom
        return Fraction(top, bottom)

    def __float__(self):
        """Return a float representation of
        the object."""
        return self.num / self.denom

    def inverse(self):
        """Returns an inverse of my Fraction object."""
        return Fraction(self.denom, self.num)

def main():
    a = Fraction(3, 4)
    b = Fraction(1, 4)
    # d = Fraction(3.14, 6)
    print(a, b)
    c = a + b
    print(c)
    print(a.__float__())
    print(float(c))
    print(Fraction.__float__(a))
    print(b.inverse())
    print(float(a.inverse()))
    # a * b


main()
