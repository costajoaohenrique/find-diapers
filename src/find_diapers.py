from src.finders.finder_factory import FinderFactory
from src.repository.diaper_repository import DiaperRepository
import schedule
import time


class FindDiapers:

    def __init__(self):
        self._list_diapers = list()
        self._repository = DiaperRepository()

    def find_all(self):
        print("Iniciando Busca de Diapers")
        print("Obtendo Finders....")
        finders = FinderFactory.get_finders()
        print(f"Encontrado {len(finders)} Finders")
        for finder in finders:
            self._list_diapers.extend(finder.find())

    def save_all(self):
        print(f"Obtidos {len(self._list_diapers)} Diapers")
        print("Gravando Diapers")
        for diaper in self._list_diapers:
            diaper_found = self._repository.find_by_sku(diaper.sku)
            new_price = diaper.prices[0]
            if diaper_found and not diaper_found.exist_price_in_date(new_price.date):
                diaper_found.add_price(diaper.prices[0])
                diaper = diaper_found
            self._repository.save(diaper)


def run():
    print("Iniciando Worker do Find Diapers")
    find_diapers = FindDiapers()
    find_diapers.find_all()
    find_diapers.save_all()


if __name__ == "__main__":
    # schedule.every(1).minutes.do(run)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    run()