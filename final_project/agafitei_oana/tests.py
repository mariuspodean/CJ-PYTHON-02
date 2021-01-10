from application import Bouquet, PrettyBouquet, BouquetBox, enter_store
import unittest

class BouquetTest(unittest.TestCase):

    def test_adding_two_disjoint_bouquets(self):
        b1 = Bouquet("Bouquet 1",{"flower 1":1,"flower 2":2})
        b2 = Bouquet("Bouquet 2",{"flower 3":1,"flower 5":3})
        result = b1 + b2
        
        assert result.bouquet_name == "Bouquet 1 and Bouquet 2"
        assert result.bouquet_flowers.__contains__("flower 1")
        assert result.bouquet_flowers.__contains__("flower 2")
        assert result.bouquet_flowers.__contains__("flower 3")
        assert result.bouquet_flowers.__contains__("flower 5")
        assert result.bouquet_flowers["flower 1"] == 1
        assert result.bouquet_flowers["flower 2"] == 2
        assert result.bouquet_flowers["flower 3"] == 1
        assert result.bouquet_flowers["flower 5"] == 3
        
    def test_adding_two_overlapping_bouquets(self):
        b1 = Bouquet("Bouquet 1",{"flower 1":1,"flower 2":2})
        b2 = Bouquet("Bouquet 2",{"flower 1":1,"flower 2":3})
        result = b1 + b2
        
        assert result.bouquet_name == "Bouquet 1 and Bouquet 2"
        assert result.bouquet_flowers.__contains__("flower 1")
        assert result.bouquet_flowers.__contains__("flower 2")
        assert result.bouquet_flowers["flower 1"] == 2
        assert result.bouquet_flowers["flower 2"] == 5

    def test_adding_two_partially_overlapping_bouquets(self):
        b1 = Bouquet("Bouquet 1",{"flower 1":1,"flower 2":2})
        b2 = Bouquet("Bouquet 2",{"flower 1":1,"flower 3":3})
        result = b1 + b2
        
        assert result.bouquet_name == "Bouquet 1 and Bouquet 2"
        assert result.bouquet_flowers.__contains__("flower 1")
        assert result.bouquet_flowers.__contains__("flower 2")
        assert result.bouquet_flowers.__contains__("flower 3")
        assert result.bouquet_flowers["flower 1"] == 2
        assert result.bouquet_flowers["flower 2"] == 2
        assert result.bouquet_flowers["flower 3"] == 3

if __name__ == '__main__':
    unittest.main()