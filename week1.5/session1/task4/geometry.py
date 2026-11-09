# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

import math

class Circle:
    """
    A circle with a centre and radius.
    """
    def __init__(self, centre, radius) -> None:
        """
        Creates a circle with a centre and radius.
        """
        self.centre = centre
        self.radius = radius

    def area(self):
        """
        Returns the area of a circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the area of a circle
        """
        return math.pi * self.radius * 2

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
        
    def distance(self):
        """Returns this point's distance from the origin."""
        return math.hypot(self.x, self.y)
    
    def distance_to(self, other_point):
        """Returns the distance from this point to another Point."""
        return math.hypot(self.x - other_point.x, self.y - other_point.y)
