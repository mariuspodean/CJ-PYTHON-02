from us1 import vector
import unittest

# def test_vector_object_attribute_initialization():
#     #  A A A
#
#     # Arrange -> Input
#     x, y = 2, 4
#
#     # Act
#     test_vector = vector.Vector(x,y)
#
#     # Assert
#     assert hasattr(test_vector, 'x'), 'Vector class is missing x attribute'
#     assert hasattr(test_vector, 'y'), 'Vector class is missing y attribute'
#
#
# def test_vector_sum_between_two_vectors_is_sum_of_indices():
#     # Arrange -> Input
#     vector1 = vector.Vector(1, 2)
#     vector2 = vector.Vector(4, 2)
#
#     # Act
#     test_sum = vector.Vector.sum(vector1, vector2)
#
#     # Assert
#     assert test_sum.x == vector1.x + vector2.x, 'X index is not valid'
#     assert test_sum.y == vector1.y + vector2.y, 'Y index is not valid'


class TestVector(unittest.TestCase):

   def test_vector_object_attribute_initialization(self):
        x, y = 2, 4

        test_vector = vector.Vector(x, y)

        assert hasattr(test_vector, 'x'), 'Vector class is missing x attribute'
        assert hasattr(test_vector, 'y'), 'Vector class is missing y attribute'


# if __name__ == '__main__':
#     unittest.main()
