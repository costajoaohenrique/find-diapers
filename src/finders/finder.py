from abc import abstractmethod
from typing import List
from src.models.diaper import Diaper
from src.config.selenium_driver import SeleniumDriver
from src.finders.finder_extra import FinderExtra

class Finder:

    @abstractmethod
    def find(self) -> List[Diaper]:
        return

    @staticmethod
    def get_finders()-> List[Finder]:
        finders = list()
        finders.append(FinderExtra(SeleniumDriver()))
        return finders