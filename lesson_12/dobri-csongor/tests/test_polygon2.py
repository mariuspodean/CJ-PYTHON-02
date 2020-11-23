import unittest

from lesson12 import polygon2

class TestPolygon(unittest.TestCase):

    def test_polygon_object_attribute_initialization(self):

        s1,s2,s3=4,6,6
        
        test_poligon = polygon2.Polygon(s1,s2,s3)

        assert hasattr(test_poligon, 's1'), 'Polygon has no Side 1'
        assert hasattr(test_poligon, 's2'), 'Polygon has no Side 2'
        assert hasattr(test_poligon, 's3'), 'Polygon has no Side 3'

    
    def test_sides_sum_equals_perimeter(self):

        pol = polygon2.Polygon(4,4,4)

        test_poligon_perimeter = pol.perimeter()

        self.assertEqual(test_poligon_perimeter, pol.s1+pol.s2+pol.s3), 'Sum is not good'

    def test_area_not_returns_none(self):

        pol = polygon2.Polygon(2,2,2)

        test_poligon_area = pol.area()

        self.assertIsNotNone(test_poligon_area), 'Area returns None'    
        self.assertFalse(isinstance((test_poligon_area),int)), 'The returned area is not an integer'