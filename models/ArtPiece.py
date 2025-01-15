class ArtPiece:
    _title: str
    _artist: str
    _year: int
    _price: float

    def __init__(self, title: str, artist: str, year: int, price: float):
        self._title = title
        self._artist = artist
        self._year = year
        self._price = price

    def get_price(self):
        return self._price
    
    def set_price(self, price: float):
        if (price < 0):
            raise ValueError("Price cannot be negative")
        self._price = price

    def __str__(self, type = "Dzieło"):
        return f"{type}: {self._title} ({self._artist}, {self._year}), Cena: {self._price} zł"