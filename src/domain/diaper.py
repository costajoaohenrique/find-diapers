from src.domain.price import Price


class Diaper:

    def __init__(self, sku, name, url_image, store, _id=None):
        self._id = _id
        self._sku = sku
        self._name = name
        self._prices = list()
        self._url_image = url_image
        self._store = store

    @property
    def id(self):
        return self._id

    @property
    def sku(self):
        return self._sku

    @property
    def name(self):
        return self._name

    @property
    def prices(self):
        return self._prices

    @property
    def url_image(self):
        return self._url_image

    @property
    def store(self):
        return self._store

    def exist_price_in_date(self, date) -> bool:
        return True if date in [price.date for price in self._prices] else False

    def add_price(self, price: Price):
        self._prices.append(price)

    def __iter__(self):
        yield '_id', self._id
        yield 'sku', self._sku
        yield 'name', self._name
        yield 'prices', [dict(price) for price in self._prices]
        yield 'url_image', self._url_image
        yield 'store', self._store

    @staticmethod
    def create_from_dict(from_dict: dict):
        diaper = Diaper(from_dict["sku"], from_dict["name"], from_dict["url_image"], from_dict["store"],
                        from_dict["_id"])
        for dict_price in from_dict["prices"]:
            diaper.add_price(Price.create_from_dict(dict_price))
        return diaper
