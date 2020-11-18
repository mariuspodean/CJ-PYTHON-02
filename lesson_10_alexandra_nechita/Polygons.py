from math import sqrt

class Polygons(object):

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f'{no_of_sides} is the number of sides'

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f'Side {side_index} with length: {length}')

class PerimeterMixin:
    def perimeter (self):
        perim = sum(self.sides)
        return perim
        
        
class Triangle(Polygons, PerimeterMixin):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side1, side2, side3 = self.sides
        semi_perimeter = sum(self.sides) / 2
        return (semi_perimeter*(semi_perimeter - side1)*(semi_perimeter - side2)*(semi_perimeter - side3))** 0.5


class Square(Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return side ** 2
    
    @classmethod
    def from_area(cls, area):
        side = float(sqrt(area))
        return cls(side, side, side, side)
      
    def __str__(self):
        super().display()
        return 'A square has 4 equal sides'

my_triangle = Triangle(7, 9, 17)
print(my_triangle.perimeter())

my_square = Square.from_area(47)
print(my_square)
