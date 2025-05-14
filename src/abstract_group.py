from abc import ABC, abstractmethod


class AbstractGroup(ABC):

    @abstractmethod
    def __str__(self):
        pass  # pragma: no cover
