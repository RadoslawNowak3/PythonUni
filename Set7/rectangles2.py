from points import Point
import math


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Coordinates should be x1 < x2 and y1 < y2")
        self.corner1 = Point(x1, y1)
        self.corner2 = Point(x2, y2)

    def __str__(self):
        return "({0},{1},{2},{3})".format(self.corner1.x, self.corner1.y, self.corner2.x, self.corner2.y)

    def __repr__(self):
        return "Rectangle({0},{1},{2},{3})".format(self.corner1.x, self.corner1.y, self.corner2.x, self.corner2.y)

    def __eq__(self, other):
        if (self.corner1.x == other.corner1.x and self.corner1.y == other.corner1.y and self.corner2.x == other.corner2.x and self.corner2.y == other.corner2.y):
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.corner1.x + self.corner2.x) / 2, (self.corner1.y + self.corner2.y) / 2)

    def area(self):
        return math.fabs(self.corner1.x - self.corner2.x) * math.fabs(self.corner1.y - self.corner2.y)

    def move(self, x, y):
        return Rectangle(self.corner1.x + x, self.corner1.y + y, self.corner2.x + x, self.corner2.y + y)

    def intersection(self, other):
        point1 = Point(max(self.corner1.x, other.corner1.x), max(self.corner1.y, other.corner1.y))
        point2 = Point(min(self.corner2.x, other.corner2.x), min(self.corner2.y, other.corner2.y))
        if point2.x <= point1.x or point2.y <= point1.y:
            raise ValueError(
                "rectangles do not intersect")
        return Rectangle(point1.x, point1.y, point2.x, point2.y)

    def cover(self, other):
        point1 = Point(min(self.corner1.x, other.corner1.x), min(self.corner1.y, other.corner1.y))
        point2 = Point(max(self.corner2.x, other.corner2.x), max(self.corner2.y, other.corner2.y))
        if point2.x <= point1.x or point2.y <= point1.y:
            raise ValueError(
                "Failed to create a rectangle covering both rectangles")
        return Rectangle(point1.x, point1.y, point2.x, point2.y)

    def make4(self):
        central_point = self.center()
        rectangle1 = Rectangle(self.corner1.x, self.corner1.y, central_point.x, central_point.y)
        rectangle2 = Rectangle(central_point.x, self.corner1.y, self.corner2.x, central_point.y)
        rectangle3 = Rectangle(self.corner1.x, central_point.y, central_point.x, self.corner2.y)
        rectangle4 = Rectangle(central_point.x, central_point.y, self.corner2.x, self.corner2.y)
        return [rectangle1, rectangle2, rectangle3, rectangle4]