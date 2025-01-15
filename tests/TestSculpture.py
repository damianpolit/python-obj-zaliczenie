from models.Sculpture import Sculpture
import unittest

class TestSculpture(unittest.TestCase):

    def setUp(self):
        self.painting = Sculpture("David", "Michał Anioł", 1504, 1000000, "marmur")
    
    def test_initialization(self):
        self.assertEqual(self.painting._title, "David")
        self.assertEqual(self.painting._artist, "Michał Anioł")
        self.assertEqual(self.painting._year, 1504)
        self.assertEqual(self.painting._price, 1000000)
        self.assertEqual(self.painting.material, "marmur")

    def test_set_price_valid(self):
        self.painting.set_price(1200000)
        self.assertEqual(self.painting.get_price(), 1200000)
    
    def test_set_price_invalid(self):
        with self.assertRaises(ValueError):
            self.painting.set_price(-500)
        
    def test_str_representation(self):
        expected_str = "Rzeźba: David (Michał Anioł, 1504), Cena: 1000000 zł, Materiał: marmur\n"
        self.assertEqual(str(self.painting), expected_str)
    
if __name__ == "__main__":
    unittest.main()
