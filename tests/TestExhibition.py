from models.Exhibition import Exhibition
from models.Painting import Painting
from models.Sculpture import Sculpture
import unittest

class TestExhibition(unittest.TestCase):

    def setUp(self):
        self.exhibition = Exhibition("Wystawa Sztuki")

    def test_initialization(self):
        self.assertEqual(self.exhibition.name, "Wystawa Sztuki")
        self.assertEqual(self.exhibition.art_pieces, [])
    
    def test_add_art_piece(self):
        self.assertEqual(self.exhibition.art_pieces, [])
        self.exhibition.add_art_piece(Painting("Mona Lisa", "Leonardo da Vinci", 1503, 1000000, "olej na płótnie"))
        self.assertEqual(len(self.exhibition.art_pieces), 1)
        self.exhibition.add_art_piece(Sculpture("David", "Michał Anioł", 1504, 5000000, "marmur"))
    
    def test_calculate_total_value(self):
        self.exhibition.art_pieces = []
        self.assertEqual(self.exhibition.calculate_total_value(), "0.00")
        self.exhibition.add_art_piece(Painting("Krzyk", "Edvard Munch", 1893, 1000000, "tempera na kartonie"))
        self.assertEqual(self.exhibition.calculate_total_value(), "1000000.00")
        wenus = Sculpture("Wenus z Milo", "nieznany", 100, 5000000, "marmur")
        self.exhibition.add_art_piece(wenus)
        self.assertEqual(self.exhibition.calculate_total_value(), "6000000.00")
        wenus.set_price(10000000)
        self.assertEqual(self.exhibition.calculate_total_value(), "11000000.00")
    
    def test_str_representation(self):
        self.assertEqual(str(self.exhibition), "Wystawa: Wystawa Sztuki\n")

if __name__ == "__main__":
    unittest.main()