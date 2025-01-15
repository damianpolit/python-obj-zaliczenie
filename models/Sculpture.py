from models.ArtPiece import ArtPiece

class Sculpture(ArtPiece):
    material: str

    def __init__(self, title, artist, year, price, material):
        super().__init__(title, artist, year, price)
        self.material = material

    def __str__(self):
        return super().__str__("Rzeźba") + f", Materiał: {self.material}\n"