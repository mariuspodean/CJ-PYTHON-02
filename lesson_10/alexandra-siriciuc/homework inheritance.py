class Polygon:

    def __init__(self, *args):
        self.sides = list(args)

    def __str__(self):
        return f'Polygon object has {len(self.sides)} sides'

    def display(self):
        for index, side in enumerate(self.sides, start=1):
            print(f'Side {index} with length: {side}')


class Triangle(Polygon):

    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def area(self):
        semi_perimeter = sum(self.sides) / 2
        return (semi_perimeter *(semi_perimeter - self.sides[0]) * (semi_perimeter - self.sides[1]) * (semi_perimeter - self.sides[2])) ** 0.5


class Square(Polygon):

    def __init__(self, side):
        super().__init__(side, side, side, side)

    def area(self):
        return self.sides[0] ** 2

    @classmethod
    def from_area(cls, area):
        cls.area = area
        return area ** 0.5
    
sq = Square.from_area(16)
print (sq)

class PerimeterMixin:

    def perimeter(self):
        return f'The perimeter for this polygon is {sum(self.sides)}'

class PolygonPerimeter(Polygon, PerimeterMixin):
    pass

tr = PolygonPerimeter(4,4,6)
print (tr.perimeter())

sq1 = PolygonPerimeter(4,2,4,2)
print (sq1. perimeter())

