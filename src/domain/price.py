class Price:

    def __init__(self, value, date):
        self._value = value
        self._date = str(date)

    @property
    def date(self):
        return self._date

    @property
    def value(self):
        return self._value

    def __iter__(self):
        yield 'value', self._value
        yield 'date', self._date

    @staticmethod
    def create_from_dict(from_dict: dict):
        return Price(from_dict["value"], from_dict["date"])
