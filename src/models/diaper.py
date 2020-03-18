class Diaper:

    def __init__(self, name, price, urlImage):
        self.__name = name
        self.__price = price
        self.__urlImage = urlImage

    def __str__(self):
        return f'{self.__name} - {self.__price} - {self.__urlImage} '

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def urlImage(self):
        return self.__urlImage
