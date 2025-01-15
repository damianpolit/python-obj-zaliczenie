from models.ArtPiece import ArtPiece
from typing import List

class Exhibition:
    name: str
    art_pieces: List[ArtPiece]

    def __init__(self, name: str):
        self.name = name
        self.art_pieces = []
    
    def add_art_piece(self, art_piece: ArtPiece):
        self.art_pieces.append(art_piece)

    def calculate_total_value(self):
        total_price = 0
        for art_piece in self.art_pieces:
            print(art_piece)
            total_price += art_piece.get_price()
        return format(total_price, ".2f")
    
    def __str__(self):
        result = f"Wystawa: {self.name}\n"
        for idx, art_piece in enumerate(self.art_pieces, 1):
            result += f"{idx}. {art_piece.__str__()}"
        return result