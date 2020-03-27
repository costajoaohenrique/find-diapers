class Diaper:

    def __init__(self, sku, name, price, url_image, store):
        self._sku = sku
        self._name = name
        self._price = price
        self._url_image = url_image
        self._store = store

    def __str__(self):
        return f'{self._name} - {self._price} - {self.url_image} '

    @property
    def sku(self):
        return self._sku

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def url_image(self):
        return self._url_image

    @property
    def store(self):
        return self._store
