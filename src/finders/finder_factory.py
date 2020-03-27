from typing import List
from src.config.selenium_driver import SeleniumDriver
from src.finders.finder import Finder
from src.finders.finder_extra import FinderExtra


class FinderFactory:

    @staticmethod
    def get_finders() -> List[Finder]:
        finders = list()
        finders.append(FinderExtra(SeleniumDriver()))
        return finders
