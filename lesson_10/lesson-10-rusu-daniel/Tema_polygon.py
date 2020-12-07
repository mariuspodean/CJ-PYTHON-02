import math

class Mixxin:
    def perim(self): 
        return sum(self.sides)

class Polygon:

    def __init__(self, *args):
        self.sides = list(args)

    def __str__(self):
        return f'Polygon object has {list(self.sides)} sides'

    def display(self):
        for index, side in enumerate(self.sides, start=1):
            print(f'Side {index} with length: {side}')
            
class PerimObject(Mixxin,Polygon):
    pass

class Triangle(Polygon):

    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def area(self):
        semi_perimeter = sum(self.sides) / 2
        return (semi_perimeter *(semi_perimeter - self.sides[0]) * (semi_perimeter - self.sides[1]) * (semi_perimeter - self.sides[2])) ** 0.5
    
    def perimeter_triangle(self):
        per=side1+side2+side3
        return per 
        


class Square(Polygon):

    def __init__(self, side):
        super().__init__(side, side, side, side)

    def area(self):
        return self.sides[0] ** 2
    
    @classmethod
    def from_area(cls, sq_area):
        sq_area = float(sq_area)
        return cls(math.sqrt(sq_area))
        


sq = Square(2)
print(sq.area())

sq= Square.from_area(49)
print(sq.sides)

print(sq.from_area(49))

pb=PerimObject(1,3,4,5,6,7)
print(pb.perim())
