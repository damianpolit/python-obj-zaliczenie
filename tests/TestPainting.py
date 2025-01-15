import unittest
from models.Painting import Painting

class TestPainting(unittest.TestCase):

    def setUp(self):
        self.painting = Painting("Mona Lisa", "Leonardo da Vinci", 1503, 1000000, "olej na płótnie")

    def test_initialization(self):
        self.assertEqual(self.painting._title, "Mona Lisa")
        self.assertEqual(self.painting._artist, "Leonardo da Vinci")
        self.assertEqual(self.painting._year, 1503)
        self.assertEqual(self.painting._price, 1000000)
        self.assertEqual(self.painting.technique, "olej na płótnie")

    def test_set_price_valid(self):
        self.painting.set_price(1200000)
        self.assertEqual(self.painting.get_price(), 1200000)

    def test_set_price_invalid(self):
        with self.assertRaises(ValueError):
            self.painting.set_price(-500)

    def test_str_representation(self):
        expected_str = "Obraz: Mona Lisa (Leonardo da Vinci, 1503), Cena: 1000000 zł, Technika: olej na płótnie\n"
        self.assertEqual(str(self.painting), expected_str)

if __name__ == "__main__":
    unittest.main()
