from points import Point
import math
class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Negative radius")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):     # "Circle(x, y, radius)"
        return "Circle({0},{1},{2})".format(self.pt.x, self.pt.y,self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return (math.pi*pow(self.radius,2))

    def move(self, x, y):
        return(Circle(self.pt.x+x,self.pt.y+y,self.radius))

    def cover(self, other):
        if  self.radius > other.radius:
            raise ValueError(
                "Put the smaller circle first")
        distance = math.sqrt(pow((self.pt.x-other.pt.x),2)-pow(self.pt.y-other.pt.y,2))
        if(self.radius+distance<=other.radius):
            return other
        theta = 1 / 2 + (other.radius - self.radius) / (2 * distance)
        new_radius = (distance+self.radius+other.radius)/2
        centerx= self.pt.x *(1-theta) + theta*other.pt.x
        centery = self.pt.y *(1-theta) + theta*other.pt.y
        center=Point(centerx,centery)
        return Circle(center.x,center.y,new_radius)