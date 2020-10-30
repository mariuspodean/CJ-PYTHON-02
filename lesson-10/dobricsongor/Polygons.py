class Polygon(object):

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        return f'Polygon has {len(self.sides)} sides'

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(Polygon):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return f'The area of this triangle is {round(((s_p*(s_p - s1)*(s_p - s2)*(s_p - s3))** 0.5),2)}.'

class PerimeterMixin:
    
    def perimeter(self):
        return f'The perimeter of this shape is {sum(self.sides)}.'

class PerimeterOfShape(PerimeterMixin, Polygon):
    pass

class Square(Polygon):

    def __init__(self, side):
        super().__init__(side, side, side, side)

    def area(self):
        return f'The area of this square is {self.sides[0] ** 2}.'


    @classmethod
    def from_area(cls, given_area):
        side = given_area / 4
        #if side%2==0:
        return cls(side)
        #else:
         #   print('The given area is not right for a square.')
            


pol = Polygon(2,4,6,8,4)
print(pol)
pol.display()

tr = Triangle(4,4,6)
print(tr)
tr.display()
print(tr.area())

tr1 = PerimeterOfShape(3,5,7)
print(tr1)
print(tr1.perimeter())


sq = Square(2)
print(sq)
sq.display()
print(sq.area())


sq2 = Square.from_area(16)
print(sq2)
sq2.display()

sq3 = Square.from_area(15)
print(sq3)
sq3.display()

sq4 = PerimeterOfShape(3,5,8,6,9)
print(sq4)
print(sq4.perimeter())
