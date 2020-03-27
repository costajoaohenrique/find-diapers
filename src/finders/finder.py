from abc import abstractmethod, ABCMeta
from typing import List

from src.domain.diaper import Diaper


class Finder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self) -> List[Diaper]:
        return
