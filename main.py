from models.Exhibition import Exhibition
from models.Painting import Painting
from models.Sculpture import Sculpture
from models.ArtPiece import ArtPiece

if __name__ == '__main__':
    print("\n===== SCENARIUSZ 1 =====\n")
    exhibition = Exhibition("Wystawa Sztuki")
    art1: ArtPiece = Painting("Mona Lisa", "Leonardo da Vinci", 1503, 1000000, "olej na płótnie")
    art2: ArtPiece = Sculpture("David", "Michał Anioł", 1504, 5000000, "marmur")
    exhibition.add_art_piece(art1)
    exhibition.add_art_piece(art2)
    print(exhibition)
    print(f"Całkowita wartość wystawy: {exhibition.calculate_total_value()} zł")
    print("Zmiana ceny obrazu Mona Lisa na 1200000 zl")
    art1.set_price(1200000)
    print(exhibition)
    print(f"Całkowita wartość wystawy: {exhibition.calculate_total_value()} zł")

    print("\n===== SCENARIUSZ 2 =====\n")
    exhibition2 = Exhibition("Wystawa Sztuki - Van Gogh")
    art3: ArtPiece = Painting("Zorza Polarna", "Vincent van Gogh", 1888, 10000000, "olej na płótnie")
    art4: ArtPiece = Painting("Słoneczniki", "Vincent van Gogh", 1889, 20000000, "olej na płótnie")
    art5: ArtPiece = Sculpture("Słonecznik", "Vincent van Gogh", 1889, 5000000, "marmur")
    exhibition2.add_art_piece(art3)
    exhibition2.add_art_piece(art4)
    exhibition2.add_art_piece(art5)
    print(exhibition2)
    print(f"Całkowita wartość wystawy: {exhibition2.calculate_total_value()} zł")
    
