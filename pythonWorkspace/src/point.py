class Point(object):
    """A class to store the x and y coordinate of a point.
    The + and = operators are overloaded to work for it

    Args:
        object (object): This class is a child of the class "object"
    """

    def __init__(self, x: int = 0, y: int = 0):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
