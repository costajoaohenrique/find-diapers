from finders.finder import Finder


class FinderDiapers:

    def __init__(self):
        self._list_diapers = list()
        self._find_all()

    def _find_all(self):
        finders = Finder.get_finders()
        for finder in finders:
            self._list_diapers.append(finder.find())
        
        print(self._list_diapers)


if __name__ == "__main__":
    FinderDiapers()