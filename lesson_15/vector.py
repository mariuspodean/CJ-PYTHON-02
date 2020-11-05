class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

    @classmethod
    def sum(cls, vector1, vector2):
        x = vector1.x + vector2.x
        y = vector1.y + vector2.y
        return Vector(x, y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)