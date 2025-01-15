from models.ArtPiece import ArtPiece

class Painting(ArtPiece):
    technique: str

    def __init__(self, title: str, artist: str, year: int, price: float, technique: str):
        super().__init__(title, artist, year, price)
        self.technique = technique

    def __str__(self):
        return super().__str__("Obraz") + f", Technika: {self.technique}\n"