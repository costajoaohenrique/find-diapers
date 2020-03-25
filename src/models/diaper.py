class Diaper:

    def __init__(self, name, price, urlImage):
        self._name = name
        self._price = price
        self._urlImage = urlImage

    def __str__(self):
        return f'{self._name} - {self._price} - {self._urlImage} '

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def urlImage(self):
        return self._urlImage
