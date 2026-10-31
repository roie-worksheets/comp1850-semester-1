# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, *args):
        """
        Creates a Rectangle, given values for width and height.
        """
        if list(map(type, args)) != [int, int]:
            raise TypeError
        elif args[0] <= 0 or args[1] <= 0:
            raise ValueError
        [self.width, self.height] = args;

    def is_square(self):
        """
        Returns whether this rectangle is a square
        """
        return self.width == self.height 

    def area(self):
        """
        Returns the area of this rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of this rectangle
        """
        return 2 * (self.width + self.height)

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
