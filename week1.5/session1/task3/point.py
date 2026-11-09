# Week 1.5, Session 1: Task 3

import math


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
        
    # Add distance() method here
    def distance(self):
        """Returns this point's distance from the origin."""
        return math.hypot(self.x, self.y)
    
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other_point):
        """Returns the distance from this point to another Point."""
        return math.hypot(self.x - other_point.x, self.y - other_point.y)


# Finally, add code here to demonstrate use of Point
point1 = Point(3, 4)
point2 = Point(6, 8)

print(point1.distance()) # 5.0
print(point1.distance_to(point2)) # 5.0