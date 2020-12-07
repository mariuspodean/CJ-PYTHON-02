import unittest
import sys

from lesson_12 import crayon_box_unittest


class TestCrayon(unittest.TestCase):
    def test_crayon_object_attribute_initialize(self):

        crayons= 'White Yellow Blue Red Green Black Brown'

        test_crayons= crayon_box_unittest.CrayonsBox(crayons)

        assert hasattr(test_crayons,'crayons'), 'Crayon class is missing crayons attribute'


    def test_crayon_attribute_islist(self):

        list_crayons_in_box='White Yellow Blue Red Green Black Brown'

        test_list_crayons_in_box = crayon_box_unittest.CrayonsBox(list_crayons_in_box)

        assert hasattr(test_list_crayons_in_box,list), 'Crayon instance is not list'

    def test_crayon_insert(self):
        list_crayons = 'White Yellow Blue Red Green Black Brown'.split()

        test_add_elem=crayon_box_unittest.CrayonsBox(list_crayons)
        test_add_elem.insert(0,'Orange')
        
        self.assertEqual(len(list_crayons) + 1, len(test_add_elem)), 'ERROR! Nothing was added to the list'


    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("Lin"), "requires Linux")
    def test_linux_support(self):
        pass

        if __name__ == '__main__':
            unittest.main()









