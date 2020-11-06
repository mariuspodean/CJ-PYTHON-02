class Polygon(object):

    def __init__(self, s1,s2,s3):
        
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        # s1, s2, s3 = self.sides
        s_p = (self.s1+self.s2+self.s3) / 2
        area = round(((s_p*(s_p - self.s1)*(s_p - self.s2)*(s_p - self.s3))** 0.5),2)
        return area

    def perimeter(self):
         return self.s1+self.s2+self.s3

