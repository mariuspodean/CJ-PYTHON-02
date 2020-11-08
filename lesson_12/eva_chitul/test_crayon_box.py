from lesson_12 import crayon_box_unittest_homework
import unittest


class TestCrayonBox(unittest.TestCase):

    def test_crayon_box_attribute_initialization(self):
        crayons = 'Red Yellow Blue White Green'.split()

        test_crayons = crayon_box_unittest_homework.CrayonsBox(crayons)

        assert hasattr(test_crayons, 'crayons'), 'CrayonBox class is missing crayons attribute'

    def test_crayon_box_attribute_initialization_is_list(self):
        crayons_list = 'Red Yellow Blue White Green'.split()

        test_crayons_list = crayon_box_unittest_homework.CrayonsBox(crayons_list)

        assert isinstance(test_crayons_list.crayons, list), 'CrayonsBox instance is not list'

    def test_crayon_box_len_method_returns_correct_integer(self):
        crayons = 'Red Yellow Blue White Green'.split()

        length_crayons = len(crayon_box_unittest_homework.CrayonsBox(crayons))

        self.assertEqual(len(crayons), length_crayons), 'CrayonsBox len function not returning correct integer'

    def test_insert_method_adds_element(self):
        crayons = 'Red Yellow Blue White Green'.split()

        crayons_instance = crayon_box_unittest_homework.CrayonsBox(crayons)
        crayons_instance.insert(2, 'Burgundy')

        self.assertEqual(len(crayons) + 1, len(crayons_instance)), 'CrayonBox insert function not adding new element'

    def test_str_method_returning_string(self):
        crayons = 'Red Yellow Blue White Green'.split()

        crayons_print = crayon_box_unittest_homework.CrayonsBox(crayons)
      
        assert isinstance(crayons_print.__str__(), str), 'Str method not returning string'
