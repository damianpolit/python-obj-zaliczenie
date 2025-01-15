from models.ArtPiece import ArtPiece
import unittest

class TestArtPiece(unittest.TestCase):
    def test_initialization(self):
        art_piece = ArtPiece("Mona Lisa", "Leonardo da Vinci", 1503, 1000000)
        self.assertEqual(art_piece._title, "Mona Lisa")
        self.assertEqual(art_piece._artist, "Leonardo da Vinci")
        self.assertEqual(art_piece._year, 1503)
        self.assertEqual(art_piece._price, 1000000)
    
    def test_set_price_valid(self):
        art_piece = ArtPiece("Mona Lisa", "Leonardo da Vinci", 1503, 1000000)
        art_piece.set_price(1200000)
        self.assertEqual(art_piece.get_price(), 1200000)
    
    def test_set_price_invalid(self):
        art_piece = ArtPiece("Mona Lisa", "Leonardo da Vinci", 1503, 1000000)
        with self.assertRaises(ValueError):
            art_piece.set_price(-500)
        
    def test_str_representation(self):
        art_piece = ArtPiece("Mona Lisa", "Leonardo da Vinci", 1503, 1000000)
        expected_str = "Dzieło: Mona Lisa (Leonardo da Vinci, 1503), Cena: 1000000 zł"
        self.assertEqual(str(art_piece), expected_str)
    
if __name__ == "__main__":
    unittest.main()